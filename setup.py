from distutils.core import setup

setup(
    name='osint_box',
    version='1.0',
    description='OSINT module',
    author='Mikhail',
    author_email='dantebudger@gmail.com',
    packages=['full_scripts'],
    package_dir={'full_scripts': 'full_scripts'},
    package_data={'full_scripts': ['*.dat']},
)
