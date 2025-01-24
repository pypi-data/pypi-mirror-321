#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()

with open('requirements.txt', 'r') as require:
    REQUIRES = require.read()

setup(
    name='pygdk',
    version='1.0.0', # MAJOR.MINOR.PATCH
    license='MIT',
    # url='',
    description='Python General Development Kit',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=REQUIRES,
    #extras_require={},
    #dependency_links=[],
    keywords="GUI,Cross-Platform, Lightweight, Fast",
    project_urls={
        # "Documentation": "",
        "Issue Tracker": "https://github.com/DevByEagle/pygdk/issues",
        "Source": "https://github.com/DevByEagle/pygdk",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        # "Operating System :: Microsoft :: Windows",
    ],
    #python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
)
