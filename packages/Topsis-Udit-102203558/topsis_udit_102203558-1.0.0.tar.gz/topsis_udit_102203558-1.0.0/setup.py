
from setuptools import setup, find_packages

setup(
    name='Topsis-Udit-102203558',
    version='1.0.0',
    author='Udit Arora',
    author_email='uditarora@example.com',
    description='A Python package for implementing the TOPSIS method.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'topsis=topsis:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
