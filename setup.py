from setuptools import setup, find_packages

setup(
    name='m',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'm=m.mover:cli',
        ],
    },
    author="Chowdhury Faizal Ahammed",
    description="A utility to rename files with wildcard support",
    keywords="m"
)
