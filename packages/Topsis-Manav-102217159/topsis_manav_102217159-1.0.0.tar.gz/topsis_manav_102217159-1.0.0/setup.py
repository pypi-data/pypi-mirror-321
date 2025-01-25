from setuptools import setup, find_packages

setup(
    name='Topsis-Manav-102217159',  # Package name
    version='1.0.0',
    author='Manav Chhouda',
    author_email='mchhouda_be22@thapar.edu',
    description='A Python package to implement the TOPSIS method for decision making.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/22MANAV22/Topsis-ManavChhouda-102217159',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',  # Makes your script callable from the terminal
        ],
    },
)


