from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

setup(
    name="Topsis-Nitin-102203984", 
    version="1.0.0",
    author="Nitin Singla",  
    author_email="nitinsingla702@gmail.com",  
    description="A Python package for implementing the TOPSIS method.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/singla-nitin/Topsis-Nitin-102203984", 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'topsis=topsis_module.main:main',  # Adjust if your main script is located elsewhere
        ],
    },
)