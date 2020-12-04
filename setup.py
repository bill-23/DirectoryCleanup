from setuptools import setup, find_packages

setup(
    name='organize',
    version='0.1',
    py_modules=['organize'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        organize=organize:organize_dir
    ''',
)