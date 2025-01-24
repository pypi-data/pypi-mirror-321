from setuptools import setup, find_packages

setup(
    name="db_operationsss",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'psycopg2',
    ],
    author="Unberkannt",
    author_email="unberkannt@mail.ru",
    description="A library for performing database operations with PostgreSQL",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Unberkannt/db_operationsss",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)