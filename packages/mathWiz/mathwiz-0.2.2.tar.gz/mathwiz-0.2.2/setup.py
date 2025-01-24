from setuptools import setup, find_packages

setup(
    name='mathWiz',
    version='0.2.2',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    description='A python math module designed for complex math.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='William E.',
    author_email='williamemerick10@gmail.com',
    url='https://github.com/William-deg/mathWiz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
