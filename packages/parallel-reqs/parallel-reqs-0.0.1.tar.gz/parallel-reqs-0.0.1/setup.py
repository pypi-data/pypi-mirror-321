from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Call parallel request Pyhton'

setup(
    name="parallel-reqs",
    version=VERSION,
    packages=find_packages(include=['paralle_reqs']),
    install_requires=[
        "aiohttp",
    ],
    entry_points={
        'console_scripts': [
            'run=parallel_reqs.main:main',
        ],
    },
    package_dir={'': 'parallel_reqs'},
    include_package_data=True,
    author="Daniele Frulla",
    author_email="daniele.frulla@newstechnology.eu",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tuo_username/parallel_requests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
