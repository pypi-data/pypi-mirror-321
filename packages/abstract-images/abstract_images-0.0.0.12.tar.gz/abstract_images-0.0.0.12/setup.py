
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='abstract_images',
    version='0.0.0.12',
    author='putkoff',
    author_email='partners@abstractendeavors.com',
    description="This module, part of the `abstract_essentials` package, provides a collection of utility functions for working with images and PDFs, including loading and saving images, extracting text from images, capturing screenshots, processing PDFs, and more.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AbstractEndeavors/abstract_images',
    package_dir={"": "src"},
    packages=find_packages(where="src"),

    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.11',
      ],
    install_requires=['pyscreenshot>=3.1',
                      'abstract_utilities>=0.1.7',
                      'numpy>=1.25.2',
                      'PyPDF2>=3.0.1',
                      'setuptools>=66.1.1',
                      'pdf2image>=1.16.3',
                      'abstract_gui>=0.0.55.6',
                      'abstract_webtools>=0.1.0',
                      'pytesseract>=0.3.10'],
    extras_require={
        "dev": ["pytest", "flake8", "mypy"],
    },
    python_requires=">=3.6",
    license="MIT",
    license_files=("LICENSE",),
    setup_requires=["wheel"],
)
