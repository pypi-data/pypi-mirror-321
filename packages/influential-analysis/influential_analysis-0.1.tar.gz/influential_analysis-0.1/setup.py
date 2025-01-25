from setuptools import setup, find_packages

setup(
    name="influential-analysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "seaborn",
        "matplotlib",
        "scikit-learn",
        "fairlearn"
    ],
    author="Blazhe manev",
    description="A library for finding influential instances in ML models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BlazheManev/bm-influential-instance-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
