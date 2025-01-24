from setuptools import setup, find_packages

setup(
    name="techv_ai",
    version="0.1.0",
    description="TechV.AI Python package for Groq-based LLM integration.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Pitambar Muduli",
    author_email="pitambar.muduli@techvantagesystems.com",
    url="https://github.com/pitmabar/techv_ai",
    packages=find_packages(),
    install_requires=[
        "groq-sdk>=1.0.0",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
