from setuptools import setup, find_packages
import os

# Read the contents of README.md
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='predictive_modeling_auto',
    version='0.2.1',
    author='Ashish Shimpi',
    author_email='a.shimpi93@gmail.com',
    description='A package for automating predictive modeling tasks using Python',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/ashishs1407/predictive_modeling_auto',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    project_urls={
        'Source': 'https://github.com/ashishs1407/predictive_modeling_auto',
        'Tracker': 'https://github.com/ashishs1407/predictive_modeling_auto/issues',
    },
    install_requires=[
        # List your package dependencies here
    ],
    python_requires='>=3.6',
)