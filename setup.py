from setuptools import setup

setup(
    name='mylib',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:rletendu/mylib.git',
    author='Raphael Letendu',
    author_email='raphael.letendu@gmail.com',
    license='unlicense',
    packages=['mylib'],
    zip_safe=False
)