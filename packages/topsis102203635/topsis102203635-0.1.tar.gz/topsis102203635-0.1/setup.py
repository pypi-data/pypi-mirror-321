from setuptools import setup, find_packages

setup(
    name='topsis102203635',
    version='0.1',
    description='Package to perform TOPSIS Analysis',
    author='Samrath Singh',
    author_email='skharbanda_be22@thapar.edu',
    url='https://github.com/DSam327/topsis102203635/',
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
