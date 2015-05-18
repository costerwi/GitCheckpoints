from setuptools import setup

setup(name='gitcheckpoints',
    version='0.1',
    description='Git based checkpoints for IPython',
    url='https://github.com/csiro-scientific-computing/gitcheckpoints',
    author='Alex Kruger',
    author_email='Alex.Kruger@csiro.au',
    license='CSIRO BSD MIT',
    packages=['gitcheckpoints'],
    install_requires = ['ipython>=3'],
    classifiers=['Development Status :: 4 - Beta'],
    zip_safe=False)
