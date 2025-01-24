from setuptools import setup, find_packages

setup(
    name='dashpaan',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        line.strip() for line in open('requirements.txt').readlines() if line.strip()
    ],
    author='Monirs.co',
    author_email='connect@monirs.com',
    description='Dashpaan is a Python package designed for creating dynamic dashboards and web pages with minimal code. It provides a wide range of UI components (elements) that can be easily integrated into web applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/monirs/dashpaan',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
