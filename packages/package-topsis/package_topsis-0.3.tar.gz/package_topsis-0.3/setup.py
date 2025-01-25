from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="package_topsis",  
    version="0.3",  
    description="A Python package for performing TOPSIS analysis",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    author="Manya Chhabra", 
    author_email="your_email@example.com",  
    url="https://github.com/your_username/package_topsis",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
    ],
    python_requires=">=3.6",  
    install_requires=[
        "numpy>=1.18.0",  
    ],
    project_urls={  
        "Bug Tracker": "https://github.com/your_username/package_topsis/issues",
        "Documentation": "https://github.com/your_username/package_topsis",
        "Source Code": "https://github.com/your_username/package_topsis",
    },
)
