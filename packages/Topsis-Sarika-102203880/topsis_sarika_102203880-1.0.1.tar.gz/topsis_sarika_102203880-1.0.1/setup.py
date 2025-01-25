from setuptools import setup, find_packages

setup(
    name='Topsis-Sarika-102203880',
    version='1.0.1',
    author='Sarika',
    author_email='sarika090903@gmail.com',  # Update this to your new email
    description='A Python package for TOPSIS decision making.',
   long_description=open("README.md", encoding="utf-8").read(),

    long_description_content_type='text/markdown',
    url='https://github.com/Sarikaa9/Topsis-Sarika-102203880.git',  # Update this to your new GitHub URL
    packages=find_packages(),
    install_requires=['numpy', 'pandas'],
)

