import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simulpy",
    version="0.0.1",
    author="Arjun Sahdev",
    author_email="arjunsahdev13@gmail.com",
    description="A small package for robot simulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kaneki99/simulpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
