from setuptools import setup, find_packages

setup(
    name="lucifer7",
    version="0.1.0",
    description="A simple calculator package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Manas Chopra",
    author_email="manaschopra95826@gmail.com",
    url="https://github.com/manas95826/lucifer7",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)