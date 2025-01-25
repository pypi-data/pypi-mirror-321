from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="package_102217249",  
    version="1.0.0",  
    description="A Python package for performing TOPSIS analysis",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    author="Manya Chhabra", 
    author_email="your_email@example.com",  
    url="https://github.com/your_username/package_102217249",  
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
        "Bug Tracker": "https://github.com/your_username/package_102217249/issues",
        "Documentation": "https://github.com/your_username/package_102217249",
        "Source Code": "https://github.com/your_username/package_102217249",
    },
)
