from setuptools import setup, find_packages

setup(
    name='sql_testing_tools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'sqlparse>=0.5.1',
        'requests>=2.32.3'
    ],
    package_data={
        'sql_testing_tools': ['databases/*.db'],
    },
    include_package_data=True,
)