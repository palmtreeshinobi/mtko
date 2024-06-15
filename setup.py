from setuptools import setup, find_packages

setup(
    name='mtko',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'mtko=mtko.main:main',
        ],
    },
)