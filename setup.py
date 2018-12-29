from setuptools import setup

setup(
    name='drop_token',
    version='0.1.0',
    packages=['drop_token'],
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['start = drop_token.cli:main']})
