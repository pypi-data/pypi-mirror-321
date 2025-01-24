import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='shiny-imagestore',
    version='3.2.0',
    packages=find_packages(),
    install_requires=[
        'django>=2.2',
        'pillow>=5.4.1',
        'sorl-thumbnail>=12.4.0',
        'django-autocomplete-light>=3.0',
        'django-tagging',
        'swapper',
        'faust-cchardet>=2.1.9',
    ],
    author='Pavel Zhukov',
    author_email='gelios@gmail.com',
    description='Gallery solution for django projects',
    long_description=README,
    long_description_content_type='text/markdown',
    license='BSD 3-Clause',
    keywords='django gallery',
    url='https://github.com/PSzczepanski1996/shiny-imagestore',
    include_package_data=True
)
