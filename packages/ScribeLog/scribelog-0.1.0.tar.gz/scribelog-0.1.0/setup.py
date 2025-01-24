from setuptools import setup, find_packages

setup(
    name='ScribeLog',
    version='0.1.0',
    author='RosebudSystems',
    author_email='ale.javier.romero@gmail.com',
    description='A lightweight Python library for logging messages to text files.',
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rosebudsystems/ScribeLog', 
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
