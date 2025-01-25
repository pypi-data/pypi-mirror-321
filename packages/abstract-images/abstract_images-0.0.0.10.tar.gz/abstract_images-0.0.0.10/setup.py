
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='abstract_images',
    version='0.0.0.10',
    author='putkoff',
    author_email='partners@abstractendeavors.com',
    description="This module, part of the `abstract_essentials` package, provides a collection of utility functions for working with images and PDFs, including loading and saving images, extracting text from images, capturing screenshots, processing PDFs, and more.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AbstractEndeavors/abstract_images',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "abstract_solcatcher": ["database_calls/*.json"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
    ],
    install_requires=[
        "abstract_utilities",
        "abstract_solana",
        "abstract_apis",
        "requests",
        "abstract_security",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "mypy"],
    },
    python_requires=">=3.6",
    license="MIT",
    license_files=("LICENSE",),
    setup_requires=["wheel"],
)
