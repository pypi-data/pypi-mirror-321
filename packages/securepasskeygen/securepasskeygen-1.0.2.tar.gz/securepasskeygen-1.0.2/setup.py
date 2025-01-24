from setuptools import setup, find_packages

setup(
    name='securepasskeygen',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[],
    description='A secure password generator using modern standards.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Emil Holmgaard',
    author_email='emil@holmgaard.io',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
