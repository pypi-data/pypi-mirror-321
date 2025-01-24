from setuptools import setup, find_packages

setup(
    name="Gptmodule",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow",
        "transformers",
        "tqdm",
        "psutil"
    ],
    description="A private module for dataset loading and GPT training.",
    author="Boring._.wicked",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)