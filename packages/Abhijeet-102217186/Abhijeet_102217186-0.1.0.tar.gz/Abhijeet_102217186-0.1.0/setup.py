from setuptools import setup, find_packages

setup(
    name="Abhijeet_102217186",
    version="0.1.0",
    description="TOPSIS Python Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abhaijeet Singh",
    author_email="asingh37_be22@thapar.edu",
    url="https://github.com/AbhaijeetSingh11/102217186_abhaijeet_topsis",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",  # Ensure the `main()` function exists in topsis.py
        ],
    },
    python_requires=">=3.6",
)
