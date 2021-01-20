from setuptools import setup, find_packages
from sys import argv

install_requires = [
    'alvadescpy==0.1.0',
    'padelpy==0.1.8'
]

if '--omit_tf' in argv:
    argv.remove('--omit_tf')
else:
    install_requires.append('h5py==2.10.0')
    install_requires.append('tensorflow==2.0.0')

setup(
    name='ecpredict',
    version='0.1.4',
    description='UMass Lowell Energy and Combustion Research Laboratory '
                'Pre-built Models',
    url='https://github.com/ecrl/ecpredict',
    author='Travis Kessler',
    author_email='Travis_Kessler@student.uml.edu',
    license='MIT',
    packages=find_packages(),
    python_requires='~=3.7',
    install_requires=install_requires,
    package_data={'ecpredict': ['models/*']},
    zip_safe=False
)
