from setuptools import setup, find_packages

setup(
    name="sql_library",
    version="0.6",
    packages=find_packages(),
    install_requires=["psycopg2"],
    author="Alexey Kalinin",
    author_email="kad2005@list.ru",
    description="A simple library for working with PostgreSQL",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)