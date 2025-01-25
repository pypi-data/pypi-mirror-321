from setuptools import setup, find_packages

setup(
    name="Topsis-Nitin_Goyal-102203614",  
    version="0.1.0",
    author="Nitin Goyal", 
    author_email="goyalnitin126@gmail.com", 
    description="A Python package for implementing the TOPSIS method",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/goyal786/Topsis-Nitin_goyal-102203614",  # Replace with your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
