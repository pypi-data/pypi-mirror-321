from setuptools import setup, find_packages

setup(
    name="Topsis-Chahat_Garg-102203557",
    version="0.1.0",
    author="Chahat Garg",
    author_email="gargchahat2005@gmail.com",
    description="A Python package for implementing the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chahatgarg884/Topsis-102203557-Chahat_Garg",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
    ],
)
