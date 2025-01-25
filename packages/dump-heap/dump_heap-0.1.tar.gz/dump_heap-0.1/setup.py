# setup.py

from setuptools import setup

setup(
    name='dump_heap',
    version='0.1',
    py_modules=['dump_heap'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dump_heap = dump_heap:main',
        ],
    },
)

