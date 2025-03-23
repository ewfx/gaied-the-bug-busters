from setuptools import setup, find_packages

setup(
    name="gaied-the-bug-busters",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "langchain",
        "transformers",
        "torch",
        "pytesseract",
        "pdf2image",
        "pytest"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "mypy",
            "black",
            "isort",
            "flake8"
        ]
    }
)