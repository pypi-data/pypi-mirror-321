from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='levellogger',
    version='0.2.4',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'typing'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)