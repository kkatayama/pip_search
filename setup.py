import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pip-search-color',
    version='0.2.7',
    author='Teddy Katayama',
    author_email='katayama@udel.edu',
    description='Wrapper for "pip search" with color and hyperlink features.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/kkatayama/pip_search',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["rich", "bs4", "requests"],
    entry_points={
        'console_scripts': [
            'pip_search=pip_search.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
