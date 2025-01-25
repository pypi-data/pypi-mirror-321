from setuptools import setup, find_packages

# Read the README file with UTF-8 encoding
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='topsis102203635',
    version='0.1.4',
    description='Package to perform TOPSIS Analysis',
    author='Samrath Singh',
    author_email='skharbanda_be22@thapar.edu',
    url='https://github.com/DSam327/topsis102203635/',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
