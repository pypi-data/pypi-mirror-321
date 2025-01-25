from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    description = f.read()

setup(

    name= "test_1_pedro",
    version= "0.0.1",
    packages=find_packages(), install_requires=[
        # Add dependencies here.
        # e.g. 'numpy >= 1.11.1'
    ],
    long_description=description,
    long_description_content_type='text/markdown',
)

