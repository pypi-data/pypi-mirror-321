from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="TOPSIS-GAURANSH-102203322",  # Replace with your package name
    version="1.0.0",  # Initial version
    author="Gauransh Mehra",  # Replace with your name
    author_email="gmehra_be22@thapar.edu",  # Replace with your email
    description="A Python package to implement the TOPSIS method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ppi-topsis",  # Replace with your GitHub repository URL
    packages=find_packages(),  # Automatically find and include all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "topsis=TOPSIS_GAURANSH_102203322.topsis:main",  # Command-line tool entry point
        ],
    },
)
