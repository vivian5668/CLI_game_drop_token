from setuptools import setup

setup(
    name = 'drop_token',
    version = '0.1.0',
    packages = ['drop_token'],
    entry_points = {
        'console_scripts': [
            'start = drop_token.__main__:main'
        ]
    })
