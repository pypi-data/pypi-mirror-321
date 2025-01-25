from setuptools import setup, find_packages

setup(
    name='Topsis-Yashvi-102203529',
    version='1.0.0',
    author='Yashvi',
    author_email='yyashvi_be22@thapar.edu',
    description='A Python package for implementing the TOPSIS method.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Yashvihooda/Topsis-Yashvi-102203529',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
    license="MIT",
)
