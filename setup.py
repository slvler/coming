import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unsplash-service",
    version="0.1.0",
    author="slvler",
    author_email="slvler@proton.me",
    description="This package provides a convenient wrapper to the Unsplash API for python applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slvler/python-unsplash-service",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.6',
    install_requires=["urllib3==2.0.0"]
)