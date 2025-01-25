from setuptools import setup, find_packages

setup(
    name="topsis-Prince-3619",
    version="1.2.0",
    author="Prince",
    author_email="pprince_be22@thapar.edu",
    description="A Python package to implement the TOPSIS method for decision making.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Prince-05/TOPSIS",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "topsis=Topsis.__main__:main",
        ]
    },
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
