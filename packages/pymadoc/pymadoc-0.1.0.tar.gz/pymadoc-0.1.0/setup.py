from setuptools import setup, find_packages

setup(
    name="pymadoc",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "zenodo_get",
        "pandas",
        "requests",
        "humanize",
        "wget"
    ],
    author="Aleksandar",
    author_email="",  # Add your email if you want
    description="Python package to download and combine parts of MADOC dataset",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aleksandarskrbic/pyMADOC",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pymadoc=pymadoc.cli:main",
        ],
    },
) 