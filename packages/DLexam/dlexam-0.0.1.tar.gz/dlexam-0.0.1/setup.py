from setuptools import setup,find_namespace_packages
from os import listdir

version = '0.0.1'

setup(
    name = 'DLexam',
    version=version,
    url='https://https://github.com/solar-hedgehog/tve',

    author='Ryabov Pavlusha',
    author_email='9753124680sh@gmail.com',

    license='MIT',
        
    packages= ['DLexam'],

    include_package_data=True,  # Include data files specified in MANIFEST.in
    # package_data={
    #     '': ['pic/*.png'],  # Include all PNG files in the 'pic' directory
    # },
    package_data={},
    zip_safe=False
)