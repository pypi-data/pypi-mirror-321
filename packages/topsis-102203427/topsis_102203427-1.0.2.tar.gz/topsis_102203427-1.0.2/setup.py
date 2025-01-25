from setuptools import setup, find_packages

setup(
    name="topsis_102203427",
    version="1.0.2",
    author="Aditya Raj Singh",
    author_email="aditya003rs@gmail.com",
    description="A Python package for implementing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aditya-prog-git/TopsisPackage.git",  # Replace with your GitHub repository URL
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.19.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
    "console_scripts": [
        "topsis=topsis_package.main:topsis",
    ],
    },

)
