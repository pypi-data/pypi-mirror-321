"""Setup file for the RAGPDF package."""

from setuptools import setup, find_packages

# Define requirements directly
requirements = [
    "litellm>=1.30.3",
    "faiss-cpu>=1.7.4",
    "PyPDF2>=3.0.0",
    "numpy>=1.24.0",
    "pydantic>=2.5.0",
    "python-dotenv>=1.0.0"
]

# Read long description from README.md
try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="ragpdf",
    version="0.1.0",
    description="A package for retrieval-augmented generation using PDFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Codeium",
    author_email="support@codeium.com",
    url="https://github.com/codeium/ragpdf",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
    ],
    python_requires=">=3.8",
    keywords="rag pdf llm embeddings vector-search faiss",
    project_urls={
        "Bug Reports": "https://github.com/codeium/ragpdf/issues",
        "Source": "https://github.com/codeium/ragpdf",
    },
    include_package_data=True,
)
