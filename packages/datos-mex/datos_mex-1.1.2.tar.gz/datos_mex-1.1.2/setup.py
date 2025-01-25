from setuptools import setup
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup( 
    name='datos_mex',
    version='1.1.2',
    description='Consultor del api del Banco de México y del Instituto Nacional de Estadística y Geografía',
    author='Luis Manuel Rojas Patiño',
    author_email='luisrojaspatino5@gmail.com',
    packages=find_packages("datos_mex"),
    package_dir={"":'datos_mex'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= 'https://github.com/Lu1srojas/data_mx',
)
