from setuptools import setup, find_packages

setup(
    name='Topsis-HarshulDeepSingh-102203259',
    version='1.0.0',
    description='A Python package for performing TOPSIS analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='HARSHUL DEEP SINGH',
    author_email='singhharshuldeep@gmail.com',
    url='https://github.com/harshulxo/Topsis-Harshul-102203259',
    packages=find_packages(),
    include_package_data=True,  # Ensure all package data is included
    install_requires=['numpy', 'pandas', 'openpyxl'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)