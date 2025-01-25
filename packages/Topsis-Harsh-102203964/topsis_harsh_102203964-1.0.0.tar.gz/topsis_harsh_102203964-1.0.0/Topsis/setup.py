from setuptools import setup, find_packages

setup(
    name='Topsis-Harsh-102203964',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
    author='Harsh Tyagi',
    author_email='htyagi_be22@thapar.edu',
    description='A Python package for implementing TOPSIS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Harsh-tyagi94/Topsis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)