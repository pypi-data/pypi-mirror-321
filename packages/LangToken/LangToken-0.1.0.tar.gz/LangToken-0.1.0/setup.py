from setuptools import setup, find_packages

setup(
    name="LangToken",            
    version="0.1.0",                     
    author="S Victor Kumar",
    author_email="victor.myid@gmail.com",
    description="Word Tokenizer to create each word into token and decode back",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ictorv/word_token",  
    packages=find_packages(),           
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
