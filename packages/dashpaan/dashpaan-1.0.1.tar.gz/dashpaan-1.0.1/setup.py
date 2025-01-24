from setuptools import setup, find_packages

setup(
    name='dashpaan',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        line.strip() for line in open('requirements.txt').readlines() if line.strip()
    ],
    author='Monir.co',
    author_email='connect@monirs.com',
    description='Dashpaan is a Python package for building interactive dashboards using Flask and Django.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/dashpaan',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
