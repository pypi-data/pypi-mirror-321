from setuptools import setup, find_packages

setup(
    name='Topsis-Chahat-102203637',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis-cli=topsis.Chahat_102203637:main',  # This will be the entry point for your CLI
        ],
    },
    

    description='A Python package to implement the TOPSIS method for multi-criteria decision analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Chahat',
    author_email='cverma_be22@thapar.edu',
    url='https://github.com/Chahat-05/Topsis-Chahat-102203637.git',  # Replace with your repo URL
    license='MIT',
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',  # You can change this if you use a different license
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',  # Specifies this package only supports Python 3
],
)
