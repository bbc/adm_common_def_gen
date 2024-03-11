from setuptools import setup, find_packages

setup(
    name='ADM Common Definition Generator',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'xlrd',
        'openpyxl',
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'adm_cd_gen=adm_common_def_gen.adm_cd_gen:main',
        ]
    }
)
