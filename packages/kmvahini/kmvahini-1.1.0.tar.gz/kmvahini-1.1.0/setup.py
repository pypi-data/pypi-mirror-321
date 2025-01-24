from setuptools import setup, find_packages

setup(
    name="kmvahini",
    version="1.1.0",
    author="Manojkumar Patil",
    author_email="patil.manojkumar@hotmail.com",
    description="A Python package to scrape agricultural data from Karnataka's market website.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/patilmanojkumar/kmvahini",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "pandas",
        "tqdm",
        "lxml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
