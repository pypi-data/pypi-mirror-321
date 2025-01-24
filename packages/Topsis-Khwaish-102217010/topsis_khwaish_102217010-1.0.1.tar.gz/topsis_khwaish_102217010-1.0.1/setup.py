from setuptools import setup, find_packages

setup(
    name="Topsis-Khwaish-102217010",  
    version="1.0.1",
    license = 'MIT',
    description="A Python package to perform TOPSIS analysis",
    author="Khwaish Agarwal",        
    author_email="khwaishagarwal22@gmail.com", 
    url = 'https://github.com/khwaishagarwal/Topsis-Khwaish-102217010',
    download_url = 'https://github.com/khwaishagarwal/Topsis-Khwaish-102217010/archive/refs/tags/v1.0.1.tar.gz',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],  # Dependencies
    entry_points={
        'console_scripts': [
            'topsis=Topsis.topsis:main',  # Entry point for CLI usage
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
