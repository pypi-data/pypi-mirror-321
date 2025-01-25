from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="skleernexample",
    version="0.1.0",
    author="Hassan",
    author_email="your.email@example.com",
    description="A library to store and manage scikit-learn code examples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/skleernexample",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'scikit-learn',
        'numpy',
        'pandas'
    ],
)
