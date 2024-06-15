from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Run the post install script
        subprocess.call(['python', 'post_install.py'])

setup(
    name='mtko',
    version='0.1.1',
    description='A CLI tool for sending commands, error messages, tracebacks, and file contents directly to OpenAI GPT models without leaving your terminal.',
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
    cmdclass={
        'install': PostInstallCommand,
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
)