from setuptools import setup, find_packages

setup(
    name="Sqlsh",
    version="0.1",
    packages=find_packages(),
    author="UnwelcomeGuests",
    description="A Python library for remote SQLite database access via SSH",
    install_requires=[
        "paramiko"
    ]
)