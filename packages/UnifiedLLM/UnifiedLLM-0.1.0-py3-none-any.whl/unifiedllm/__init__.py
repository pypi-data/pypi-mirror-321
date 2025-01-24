import os
from openai import OpenAI
import anthropic
from typing import List, Dict, Any, Tuple, Union
import json
from json_repair import repair_json
import asyncio
from openai import AsyncOpenAI
from bs4 import BeautifulSoup

package_dir = os.path.dirname(__file__)
json_path = os.path.join(package_dir, 'unifiedcost.json')

PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

with open(json_path) as f:
    cost_dict = json.load(f)

class AsyncLLM:
    def __init__(self, name="async_llm"):
        self.name = name
        self.cost_dict = cost_dict  
        
    async def get_client_cost(self, model: str) -> Tuple[Union[anthropic.AsyncAnthropic, AsyncOpenAI], float, float,str]:
        ic = self.cost_dict[model]['input_cost']
        oc = self.cost_dict[model]['output_cost']
        base_url = self.cost_dict[model]['base_url']
        if base_url == "None":
            
            if "claude" in model:
                client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)
                type = "claude"
        
            elif "gpt" in model:
                client = AsyncOpenAI(api_key=OPENAI_API_KEY)
                type = "gpt"
        
        else:
            if base_url == "https://api.groq.com/openai/v1":
                KEY = GROQ_API_KEY
                type = "gpt"
                
            if base_url == "https://api.deepseek.com":
                KEY = DEEPSEEK_API_KEY
                type = "gpt"
            
            if base_url == "https://api.perplexity.ai":
                KEY = PERPLEXITY_API_KEY
                type = "ppx-online"
            
            client = AsyncOpenAI(api_key=KEY,base_url=base_url)
        return client, ic, oc, type

    async def chat_complete(self,model: str, prompt: str,system_message = "You are a helpful assistant.", temperature=0.1, max_tokens=3000, **kwargs) -> Tuple[str, float]:
        client, ic, oc, type = await self.get_client_cost(model)

        if type != "claude":
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "system", "content": system_message}, {"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )

            cost = ic * response.usage.prompt_tokens / 1e6 + oc * response.usage.completion_tokens / 1e6
            if type == "ppx-online":
                cost += 0.005  # request cost
            return response.choices[0].message.content, cost

        else:
            message = await client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_message,
                messages=[{"role": "user", "content": [{"type": "text", "text": prompt}]}]
            )

            cost = (ic * message.usage.input_tokens / 1e6 + oc * message.usage.output_tokens / 1e6)
            return message.content[0].text, cost
    
    async def batch_chat_complete(self, prompts: List[str], model: str,system_messages = List[str], avg_request_time = 5, rpm: int = 25, temperature=0.1, max_tokens=3000, **kwargs) -> List[Tuple[str, float]]:
        max_concurrent_requests = min(rpm, 60 // avg_request_time)
        semaphore = asyncio.Semaphore(max_concurrent_requests)

        async def limited_chat_complete(prompt,system_message):
            async with semaphore:
                return await self.chat_complete(prompt=prompt, model=model,system_message=system_message, temperature=temperature, max_tokens=max_tokens, **kwargs)
            
        tasks = [limited_chat_complete(prompt,system_message) for prompt,system_message in zip(prompts,system_messages)]
        return await asyncio.gather(*tasks)

class ProcessOutput:
    def __init__(self):
        pass
    
    @staticmethod
    def jsonify_llm(llm_output: str, tag_name:str) -> Dict:
        m = llm_output.replace(f'<{tag_name}>', '').replace(f'</{tag_name}>', '')
        try:
            return json.loads(m)
        except:
            try:
                return json.loads(repair_json(m))
            except:
                print("Error in jsonify_llm")
                return {}
    
    @staticmethod
    def jsonify_llm_new(llm_output:str) -> Dict:
        try:
            return json.loads(llm_output)
        except:
            try:
                return json.loads(repair_json(llm_output))
            except:
                print("Error in jsonify_llm")
                return {}
    
    @staticmethod
    def extract_within_tags(text: str, tag_name: str):
        soup = BeautifulSoup(text, 'html.parser')
        reason = soup.find_all(tag_name)
        if len(reason) > 0:
            reason = reason[0].text.replace(f'<{tag_name}>', '').replace(f'</{tag_name}>', '')
        else:
            reason = None
        return reason