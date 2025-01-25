 
from setuptools import setup, find_packages

setup(
    name="topsis-prak-3844",
    version="0.1",
    author="prakriti",
    author_email="pprakriti_be22@thapar.edu",
    description="A Python package to implement the TOPSIS method for multi-criteria decision-making.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

