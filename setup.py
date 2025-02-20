# setup.py
from setuptools import setup, find_packages

setup(
    name='general_py',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tqdm',  # Add tqdm as a requirement
    ],
    author='JackalCOB',
    author_email='jacob-couper@live.com'
    description='General python functions usable across a multitude of different projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JackalCOB/general_py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
