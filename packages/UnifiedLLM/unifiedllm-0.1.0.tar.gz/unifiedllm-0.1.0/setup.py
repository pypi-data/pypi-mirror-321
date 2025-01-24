from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="UnifiedLLM",  # Replace with your desired package name
    version="0.1.0",  # Initial version
    author="Phanindra Parashar",
    author_email="phanindraparashar@gmail.com",
    description="A library to utilize multiple Large Language Models asynchronously.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PhanindraParashar/UnifiedLLM",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",  # Update if using a different license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        "anthropic==0.43.0",
        "beautifulsoup4==4.12.3",
        "json_repair==0.18.0",
        "openai==1.59.7",
    ],
    include_package_data=True,  # Includes files specified in MANIFEST.in
)
