from setuptools import setup, find_packages

setup(
    name='plte',  # Your package name
    version='0.1',  # Initial version
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[],  # List of dependencies (empty for now)
    author='Python Master',  # Replace with your name
    author_email='srinivasskr707srinivasskr707@gmail.com',  # Replace with your email
    description='A Python package for data processing',  # Short description
    long_description=open('README.md').read(),  # Content of your README file
    long_description_content_type='text/markdown',  # Format of README file
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Replace with your license type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
