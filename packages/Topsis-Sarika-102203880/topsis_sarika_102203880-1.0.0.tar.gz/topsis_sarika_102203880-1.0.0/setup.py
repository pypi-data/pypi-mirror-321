from setuptools import setup, find_packages

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Sarika-102203880",  # Replace with your actual package name
    version="1.0.0",
    author="Sarika",
    author_email="your.email@example.com",
    description="A Python package for TOPSIS decision making.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/Topsis-Sarika-102203880",  # Replace with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
