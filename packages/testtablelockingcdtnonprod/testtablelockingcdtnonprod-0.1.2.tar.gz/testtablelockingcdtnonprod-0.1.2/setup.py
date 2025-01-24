from setuptools import setup, find_packages

setup(
    name="testtablelockingcdtnonprod",
    version="0.1.2",
    description="Custom library to support table locking",
    author="Javad Javadzade",
    author_email="JavadJavadzade@LiveNation.com",
    packages=find_packages(where="testtablelockingcdtnonprod"),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
)