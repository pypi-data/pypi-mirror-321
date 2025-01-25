from setuptools import setup, find_packages

setup(
    name='topsis_102203821',
    version='0.4',
    description='TOPSIS implementation for ranking alternatives based on multiple criteria',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Archit-29/102203821_topsis',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl',  # for reading Excel files
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis_102203821.main:main',  # Modify 'topsis.main:main' with the appropriate function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
