from setuptools import setup, find_packages

setup(
    name='printformats',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to print JSON, YAML, and dictionaries in a readable format',
    url='https://github.com/yourusername/printformats',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
