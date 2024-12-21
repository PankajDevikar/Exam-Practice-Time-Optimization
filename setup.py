from setuptools import setup, find_packages

setup(
    name="Exam Practice Time Optimization",  
    version="1.0.0",
    description="A project to analyze student activity logs and recommend optimal practice durations for different topics.",
    author="Pankaj Devikar",  
    author_email="pankaj.devikar@gmail.com"
    packages=find_packages(),  
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
