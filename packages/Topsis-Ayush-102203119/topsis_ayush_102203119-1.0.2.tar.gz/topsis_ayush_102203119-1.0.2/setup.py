from setuptools import setup, find_packages

setup(
    name='Topsis-Ayush-102203119',
    version='1.0.2',
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
    author='Ayush Panwar',
    author_email='apanwar_be22@thapar.edu',
    description='A Python package for implementing TOPSIS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ayush0126/Topsis-102203119',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)

