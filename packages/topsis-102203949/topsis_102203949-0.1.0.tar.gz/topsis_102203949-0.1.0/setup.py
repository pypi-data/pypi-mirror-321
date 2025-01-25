from setuptools import setup, find_packages

setup(
    name='topsis_102203949',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',  # Make 'main' function executable from CLI
        ],
    },
    description='A Python implementation of the TOPSIS method for multi-criteria decision analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arya Lal',
    author_email='aryalalqms@gmail.com',
    url='https://github.com/aryalal11/topsis',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
