from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="influential_analysis",
    version="0.1.2",  # 🔹 Bump version (PyPI does NOT allow overwriting versions)
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "seaborn",
        "matplotlib",
        "scikit-learn",
        "fairlearn"
    ],
    author="Blazhe Manev",
    description="A library for finding influential instances in ML models",
    long_description=long_description,
    long_description_content_type="text/markdown",  # 🔹 Make sure it's Markdown format
    url="https://github.com/BlazheManev/bm-influential-instance-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
