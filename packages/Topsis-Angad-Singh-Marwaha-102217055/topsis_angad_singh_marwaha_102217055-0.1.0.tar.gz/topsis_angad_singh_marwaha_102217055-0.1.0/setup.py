from setuptools import setup, find_packages

setup(
    name="Topsis-Angad_Singh_Marwaha-102217055",
    version="0.1.0",
    author="Angad_Singh_Marwaha",
    author_email="angadsingh2150@gmail.com",
    description="A Python package for implementing the TOPSIS method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/angad542/102217055_Angad_Marwaha.git",
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
