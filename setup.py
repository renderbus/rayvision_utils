"""Describe our module distribution to Distutils."""

# Import third-party modules
from setuptools import find_packages
from setuptools import setup


setup(
    name='rayvision_utils',
    author='Shenzhen Rayvision Technology Co., Ltd',
    author_email='',
    url='',
    package_dir={'': '.'},
    packages=find_packages('.'),
    description='',
    entry_points={},
    install_requires=[
        'future==0.17',
        'rayvision_log',
        'rayvision_api'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=['pytest==4.6', 'pytest-mock==1.10']
)