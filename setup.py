from setuptools import setup

setup(
    name='exampleapp',
    packages=['exampleapp'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)