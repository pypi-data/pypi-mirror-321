from setuptools import setup, find_packages

setup(
    name="topsis-Shivansh-102203508",
    version="1.0.0",
    author="Shivansh Gupta",
    author_email="shivanshgupta290804@gmail.com",
    description="A Python package for performing TOPSIS analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shivanshg29/Topsis",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",  # CLI command and entry point
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
