import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    required = fh.read()

requirements = ["requests<=2.21.0"]

setuptools.setup(
    name="pyWApp",
    version="0.0.2",
    author="Dark White",
    author_email="sasha.2000ibr@gmail.com",
    description="pyWApp is a selenium-based Whatsapp wrapper",
    long_description=long_description,
    install_requires=required,

    long_description_content_type="text/markdown",
    url="https://github.com/pysashapy/pyWApp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
