from setuptools import setup, find_packages

setup(
    name='Topsis-Dristi-102217188',
    version='1.0.0',
    author='Dristi Sinha',
    author_email='dsinha_be22@thapar.edu',
    description='A Python package for TOPSIS implementation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mikudristi/TOPSIS_Assignment.git',  # Add your GitHub repo URL
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
