from setuptools import setup, find_packages

setup(
    name='Optiquantfolio',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'scikit-learn',
        'deap',
        'yfinance',
    ],
    author='Jotiraditya Banerjee',
    author_email='joti.ban.2710@gmail.com',
    description='A comprehensive AI-based library for portfolio optimization',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/praetorian2710/OptiQuant',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
