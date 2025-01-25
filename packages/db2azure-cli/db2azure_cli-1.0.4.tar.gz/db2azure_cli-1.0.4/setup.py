from setuptools import setup, find_packages

setup(
    name="db2azure_cli",
    version="1.0.4",
    description="A CLI tool to upload database query results to Azure storage.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ajith D",
    author_email="ajithd78564@gmail.com",
    url="https://github.com/mr-speedster/DB2Azure-CLI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]", 
        "inquirer", 
        "yaspin", 
        "pyfiglet", 
        "tabulate"
    ],
    entry_points={
        "console_scripts": [
            "db2az=db2az.cli:app",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
