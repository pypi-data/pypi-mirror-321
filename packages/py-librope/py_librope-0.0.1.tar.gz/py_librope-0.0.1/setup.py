from setuptools import setup, Extension
import platform
import subprocess

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyrope",
    version="0.0.1",
    author="George Watson",
    author_email="gigolo@hotmail.co.uk",
    description="Python bindings for librope",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takeiteasy/pyrope",
    include_dirs="/Users/george/git/pyrope",
    ext_modules=[Extension("pyrope",
                           sources=["pyrope.c", "rope.c"],
                           extra_link_args=["-DROPE_WCHAR 1"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

