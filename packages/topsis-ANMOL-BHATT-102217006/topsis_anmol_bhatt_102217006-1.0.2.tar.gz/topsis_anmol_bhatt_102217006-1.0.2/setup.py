from setuptools import setup, find_packages

setup(
    name="topsis-ANMOL_BHATT_102217006",  # Replace with a unique name for your package
    version="1.0.2",
    author="Anmol Bhatt",
    description="A Python package for implementing the TOPSIS multi-criteria decision analysis method.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
    packages=find_packages(),  
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
