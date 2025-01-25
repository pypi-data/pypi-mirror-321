from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='predictive_modeling_auto',
    version='0.2.0',
    author='Ashish Shimpi',
    author_email='a.shimpi93@gmail.com',
    description='A short description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This ensures the README is interpreted correctly
    url='https://github.com/ashishs1407/predictive_modeling_auto',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # Add any other appropriate classifiers from the list
    ],
    project_urls={
        'Source': 'https://github.com/ashishs1407/predictive_modeling_auto',
        'Tracker': 'https://github.com/ashishs1407/predictive_modeling_auto/issues',
    },
    python_requires='>=3.6',
)