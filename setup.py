#code taken from python documentation incase we want to install required packages
from setuptools import setup, find_packages #find the packages which have constructor files,
                        #if found that becomes a local package, so we can access it

setup(
    name="us_visa",
    version="0.0.0",
    author="nehakotwal1998",
    author_email="nehajbk@gmail.com",
    packages=find_packages()
)