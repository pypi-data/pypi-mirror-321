from setuptools import setup, find_packages

setup(
    name='astridemo', 
    version='0.1.0', 
    packages=find_packages(), 
    install_requires=[ 
        'textblob',  
        'matplotlib', 
    ],
    description='A Python library for sentiment analysis and visualization', 
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',
    license='MIT', 
)
