from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bbtm",  
    version="1.0.0", 
    author="Padsala Tushal",
    author_email="padsalatushal@gmail.com",
    description="A Bug Bounty Tool Manager for managing and automating bug bounty tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/padsalatushal/bbtm",  
    packages=find_packages(), 
    include_package_data=True,  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",  
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bbtm=bbtm.bbtm:main",  
        ],
    },
)
