from setuptools import setup, find_packages

long_description = ""

setup(
    name='mtn-momo-python',
    version='1.0.0',
    description='Python library for the MTN MoMo API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/isaacrobert33/mtn-momo-python',
    author='Isaac Robert',
    author_email='isaacrobertoluwaseun@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'dependency-package1>=1.0.0',
        'dependency-package2>=2.0.0',
        
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
