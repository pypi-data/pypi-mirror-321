from setuptools import setup, find_packages

setup(
    name='topsis_arnav_102203979',
    version='1.4',
    packages=find_packages(),
    install_requires=['numpy','pandas'],  # List your dependencies here
    long_description=open('README.md').read(),  # Automatically takes content from your README file
    long_description_content_type="text/markdown",
    description="Python implementation of the TOPSIS method for multi-criteria decision analysis",
    url='https://github.com/Arnavsmayan/Topsis',
    entry_points={
        'console_scripts': [
            'topsis = topsis.main:main',  # This connects the command `topsis` to `main()` function
        ],
    },
)