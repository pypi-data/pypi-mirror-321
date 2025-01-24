from setuptools import setup, find_packages

setup(
    name='make_action',
    version='0.1',
    author="Mangozmorgan",
    long_description=open("README.md").read(),
    packages=find_packages(),
    url="https://github.com/votre_nom/my_package",
    install_requires=[
        'click',
        'pyyaml',
        'ruamel.yaml'
    ],
    entry_points={
        'console_scripts': [
            'make_action=make_action.main:main',
        ],
    },
)