from setuptools import setup, find_packages

setup(
    name="102203162-topsis",
    version="0.1.1",
    author="Raghav Manchanda",
    author_email="rmanchanda_be22@thapar.edu",
    description="A Python library for the TOPSIS decision-making method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/102203162-topsis",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
