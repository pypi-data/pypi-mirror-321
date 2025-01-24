from setuptools import setup, find_packages

setup(
    name="lyric-probe-performance",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'locust>=2.32.5',
        'requests>=2.32.3',
        'requests-toolbelt>=1.0.0',
        'urllib3>=2.2.3',
        'pyyaml>=6.0.1',
        'python-dateutil>=2.8.2', 
        'pandas>=2.0.0',  
        'pytest>=7.0.0', 
        'pytest-cov>=4.0.0' 
    ],
)