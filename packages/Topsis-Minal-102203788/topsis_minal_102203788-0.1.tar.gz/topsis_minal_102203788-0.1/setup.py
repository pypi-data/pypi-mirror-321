from setuptools import setup, find_packages

setup(
    name='Topsis-Minal-102203788',  # Replace with your package name
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'sys'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:topsis',  # Command line interface for topsis function
        ],
    },
    author='Minal',  # Your name
    author_email='mminal_be22@thapar.edu',  # Your email
    description='A Python package to implement the Topsis method for decision-making',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/minal2577/Topsis-Minal-102203788',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
