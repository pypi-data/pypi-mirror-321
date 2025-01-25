from setuptools import setup, find_packages

setup(
    name="102203774-topsis",
    version="0.6",
    description="TOPSIS implementation for best decision-making  ",
    long_description="Install it using pip install 102203774-topsis /n pass parameters in Topsis() function to find result use topsis.calculate() use can also use it at command line",
    author="Ajay",
    author_email="ajaysunaria11@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'topsis=topsis_102203774.cli:main',  # Define your CLI entry point
        ],
    },
    install_requires=[],  # List dependencies if any
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
