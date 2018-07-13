import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chatlib",
    version="0.0.1",
    author="python-b5",
    author_email="evangorman06@gmail.com",
    description="A tiny library for little chatbots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/python-b5/chatlib",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
