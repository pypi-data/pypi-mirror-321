from setuptools import setup, find_packages

setup(
    name="Topsis-Anant-102203856",  
    version="1.0.0",  
    author="Anant",
    description="A Python package to implement the TOPSIS method.",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0"
    ],
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ],  
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',  
        ],
    },
)
