from setuptools import setup, find_packages

setup(
    name="topsis_102203440", 
    version="0.1.0",
    author="Asmi Juneja",
    author_email="ajuneja_be22@thapar.edu",
    description="Testing Topsis ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/my_dummy_package",  # Optional GitHub repo
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
