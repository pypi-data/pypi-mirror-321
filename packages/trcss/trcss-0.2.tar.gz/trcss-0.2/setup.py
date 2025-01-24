from setuptools import setup, find_packages

setup(
    name='trcss',
    version='0.2',
    author='Atilla',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'trcss=trcss.main:main',  # Burada `main.py` dosyanı kullanıyoruz
        ],
    },
)