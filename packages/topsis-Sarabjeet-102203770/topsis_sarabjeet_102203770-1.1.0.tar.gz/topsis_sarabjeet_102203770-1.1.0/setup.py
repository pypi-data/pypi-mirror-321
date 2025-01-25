from setuptools import setup, find_packages

setup(
    name="topsis-Sarabjeet-102203770",
    version="1.1.0",
    author="Sarabjeet Singh",
    author_email="ssingh20_be22@thapar.edu",
    description="A Python package implementing TOPSIS method for Multi-Criteria Decision Making (MCDM)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SARAB0297/Topsis_3770",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.19.0',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    }
)