from setuptools import setup, find_packages

setup(
    name='Topsis-Ruhani-102203833', 
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',  
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:main', 
        ],
    },
    author='Ruhani Arora',
    description='TOPSIS algorithm implementation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ruhani2703/Topsis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
