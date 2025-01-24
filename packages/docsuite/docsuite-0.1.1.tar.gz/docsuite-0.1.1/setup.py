from setuptools import setup, find_packages

setup(
    name="docsuite",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Sifat Hasan",
    author_email="sihabhossan633@gmail.com",
    description="A unified library to load any document type effortlessly into LangChain for generative AI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pro-Sifat-Hasan/docsuite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)