from setuptools import setup, find_packages

def read_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="Topsis-Anchit-102203810",
    version="1.0.0",
    author="Anchit",
    author_email="anchitmehra2018@gmail.com",
    description="A Python package implementing TOPSIS method for MCDM problems",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AnMaster15/TOPSES_1",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_Anchit_102203810.topsis:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)