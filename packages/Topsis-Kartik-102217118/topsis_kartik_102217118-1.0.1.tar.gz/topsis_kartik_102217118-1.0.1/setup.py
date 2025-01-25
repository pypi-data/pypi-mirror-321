from setuptools import setup, find_packages

setup(
    name="Topsis-Kartik-102217118",  
    version="1.0.1",
    license = 'MIT',
    author="Kartik Garg",        
    author_email="kartikgarg0709@gmail.com", 
    url = 'https://github.com/kartikgarg0709/Topsis-Kartik-102217118',
    download_url = 'https://github.com/kartikgarg0709/Topsis-Kartik-102217118.git',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],  # Dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    description='''
        Topsis-Kartik-102217118 is a Python package designed to simplify multi-criteria decision-making using the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method. This tool allows users to evaluate and rank alternatives systematically, making it ideal for use in areas such as business analytics, project management, and research.  

        Key features of Topsis-Kartik-102217118 include:  
        - Intuitive integration with CSV files and Pandas DataFrames.  
        - Support for assigning custom weights and defining the impact (beneficial or non-beneficial) of each criterion.  
        - Fully automated data normalization and calculation of performance scores.  
        - A user-friendly command-line interface for fast execution.  

        Whether you are comparing product options, optimizing resource allocation, or conducting performance evaluations, Topsis-Kartik-102217118 empowers users with a reliable framework for objective decision-making.  

    '''
)