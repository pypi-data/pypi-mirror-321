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
    version="0.1.1",
    description="Retrive PDF files context for your LLM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alfred Wallace",
    author_email="alfred.wallace@netcraft.fr",
    url="https://github.com/alfredwallace7/ragpdf",
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
    keywords="rag pdf llm embeddings vector-search faiss context retrieval augmented generation",
    project_urls={
        "Bug Reports": "https://github.com/alfredwallace7/ragpdf/issues",
        "Source": "https://github.com/alfredwallace7/ragpdf",
    },
    include_package_data=True,
)
