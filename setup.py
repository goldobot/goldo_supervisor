from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    scripts=['nodes/node'],
    packages=[],
    )
    
setup(**setup_args)