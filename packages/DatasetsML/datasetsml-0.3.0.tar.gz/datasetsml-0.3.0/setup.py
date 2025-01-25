from setuptools import setup, find_packages

setup(
    name="DatasetsML",  
    version="0.3.0",  
    description="Datasets for ML models",
    author="Schneider",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_package",  
    packages=find_packages(),  
    install_requires=[  
        "pgmpy",       
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
)
