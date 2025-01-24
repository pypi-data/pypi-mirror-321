from setuptools import setup, find_packages

setup(
    name="atibotlog",  # Package name
    version="0.1.3",        # Initial version
    description="A Python package for bot automation and database logging.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Shibli M.S",
    packages=find_packages(),  # Automatically find packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "pandas",
        "pyodbc",
        "sqlalchemy"
    ],
    python_requires=">=3.12",
)
