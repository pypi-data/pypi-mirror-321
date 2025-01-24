from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="airtrain",
    version="0.1.0",
    author="Dheeraj Pai",
    author_email="helloworldcmu@gmail.com",
    description="A platform for building and deploying AI agents with structured skills",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rosaboyle/airtrain.dev",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
        "PyYAML>=5.4.1",
        "firebase-admin>=5.0.0",  # Optional, only if using Firebase
        "loguru>=0.5.3",  # For logging
    ],
)
