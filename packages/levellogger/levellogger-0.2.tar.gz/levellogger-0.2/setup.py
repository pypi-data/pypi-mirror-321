from setuptools import setup, find_packages

setup(
    name='levellogger',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'typing'
    ],
)