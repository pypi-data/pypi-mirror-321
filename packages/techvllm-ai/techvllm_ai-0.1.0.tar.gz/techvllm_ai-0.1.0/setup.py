from setuptools import setup, find_packages

setup(
    name="techvllm_ai",  # Package name should already be updated
    version="0.1.0",  # Increment the version here
    description="TechVLLM.AI Python package for Groq-based LLM integration.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Pitambar Muduli",
    author_email="pitambar.muduli@techvantagesystems.com",
    url="https://github.com/pitmabar/techvlm_ai",
    packages=find_packages(),
    install_requires=[
        "groq>=0.15.0",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

