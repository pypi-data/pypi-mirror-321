from setuptools import setup, find_packages

setup(
    name='scumpy',
    version=1.8,
    packages=find_packages(),
    install_requires=[
        'sympy>=1.13.1'
    ]   
)