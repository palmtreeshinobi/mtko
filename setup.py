from setuptools import setup, find_packages

setup(
    name='mtko',
    version='0.1.7',
    description='A CLI tool for sending commands, error messages, tracebacks, and file contents directly to OpenAI GPT models without leaving your terminal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Van',
    url='https://github.com/palmtreeshinobi/mtko/',
    project_urls={
        'Source Code': 'https://github.com/palmtreeshinobi/mtko/',
    },
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'mtko=mtko.main:main',
            'mtko-setkey=mtko.env_setup:setup_env',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
)