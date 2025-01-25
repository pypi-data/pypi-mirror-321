from setuptools import setup, find_packages

setup(
    name='Topsis_AarushPruthi_102203793',
    version='1.0.2',
    author='Aarush Pruthi',
    author_email='apruthi_be22@thapar.edu',
    description='A Python package for TOPSIS implementation, by Aarush Pruthi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arwoooooosh/Topsis_Assignment.git',  # Add your GitHub repo URL
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
