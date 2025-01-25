from setuptools import setup, find_packages

setup(
    name="topsis-Aarushi-102216107",
    version="1.0.0",
    author="Aarushi Gupta",
    author_email="agupta24_be22@thapar.edu",
    description="A Python package to calculate TOPSIS score.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/aarushi1610/topsis-package",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__init__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
