from setuptools import setup, find_packages

setup(
    name="mydatabase",
    version="0.1.0",
    description="Библиотека для подключения к PostgreSQL",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Андрей",
    author_email="andrey960123@gmail.com",
    url="https://www.python.org",
    packages=find_packages(),
    install_requires=[
        "psycopg2",
        "PyQt5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
