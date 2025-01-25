from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='tail-rating-py',
    version='0.1.3',
    packages=find_packages(),
    install_requires=required,
    author='Bruno Adam',
    author_email='bruno.adam@pm.me',
    description='A Python package designed to assess TAIL (Thermal, Acoustic, Indoor Air Quality, and Lighting) for buildings.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    license='GNU General Public License v3 (GPLv3)',
    keywords='tail thermal acoustic indoor air quality lighting',
    # The folder is called TAIL, but the package is called TAILpy
    package_dir={'TAIL': 'TAIL'},
)