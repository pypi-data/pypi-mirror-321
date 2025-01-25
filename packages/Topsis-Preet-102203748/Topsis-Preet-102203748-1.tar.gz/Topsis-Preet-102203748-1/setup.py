from setuptools import setup, find_packages

setup(
    name="Topsis-Preet-102203748",  # Name of your package
    version="01",  # Version of your package
    author="Preet",  # Your name
    author_email="pchaudhary_be22@thapar.edu",  # Your email
    description="A Python package for implementing TOPSIS.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis",  # Your repository URL
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0",
        "numpy>=1.19"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
