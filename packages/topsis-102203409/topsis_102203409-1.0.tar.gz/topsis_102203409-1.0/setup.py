from setuptools import setup, find_packages

setup(
    name="topsis_102203409",
    version="1.0",
    author="Arin Goyal",
    author_email="aringoyal15@gmail.com",
    description="A Python package for implementing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AGtheOG/TopsisPackagePypi",  # Replace with your GitHub repository URL
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
