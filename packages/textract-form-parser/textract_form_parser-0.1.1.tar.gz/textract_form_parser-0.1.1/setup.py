from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="textract-form-parser",
    version="0.1.1",
    author="Yogeshvar Senthilkumar",
    author_email="yogeshvar@icloud.com",
    description="A Python library for parsing AWS Textract form output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yogeshvar/text-extractor",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "boto3>=1.26.0",
        "pandas>=1.3.0",
        "numpy>=1.19.0",
        "requests>=2.25.0",
        "packaging>=20.0",
    ]
) 