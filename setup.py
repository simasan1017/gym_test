from setuptools import setup, find_packages
import sys, os

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym_test'))
from package_info import USERNAME, VERSION

setup(name='{}_{}'.format(USERNAME, 'gym_test'),
    version=VERSION,
    description='Test downloadable user environments',
    url='https://github.com/ppaquette/gym_test',
    author='Philip Paquette',
    author_email='pcpaquette@gmail.com',
    license='MIT License',
    packages=[package for package in find_packages() if package.startswith(USERNAME)],
    zip_safe=False,
    install_requires=[ 'gym>=0.2.3' ],
)
