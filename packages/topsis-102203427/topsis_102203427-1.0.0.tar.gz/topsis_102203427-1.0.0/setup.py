from setuptools import setup, find_packages

setup(
    name="topsis_102203427",  # Package name (unique on PyPI)
    version="1.0.0",         # Package version
    author="Your Name",      # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="A Python package for implementing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis_102203427",  # Replace with your GitHub repository URL
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.19.0"
    ],  # Dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "topsis=topsis_package.main:topsis",  # Command-line interface
        ],
    },
)
