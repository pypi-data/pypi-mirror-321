from setuptools import find_packages, setup

setup(
    name="ziploc",
    version="0.0.2",
    description="Credential management tool for Python backend",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Xu Ha",
    author_email="cshaxu@gmail.com",
    url="https://github.com/cshaxu/ziploc",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ziploc=ziploc.cli:main",  # CLI entry point
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pycryptodome>=3.10"  # Add any required libraries here
    ],
)
