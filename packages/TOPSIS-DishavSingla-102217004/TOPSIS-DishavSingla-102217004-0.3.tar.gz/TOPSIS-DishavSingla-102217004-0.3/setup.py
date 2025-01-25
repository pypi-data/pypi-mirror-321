from setuptools import setup, find_packages

setup(
    name="TOPSIS-DishavSingla-102217004",
    version="0.3",
    author="Dishav",
    author_email="dsingla2_be22@thapar.edu",
    description="A Python package for implementing the TOPSIS decision-making method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DISHAVSINGLA/Topsis-Dishav-102217004",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main", 
        ],
    },
)
