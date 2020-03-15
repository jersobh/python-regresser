import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regresser",
    version="0.0.2",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="A visual regression library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/python-regresser",
    install_requires=["selenium", "wand", "chromedriver-binary"],
    packages=setuptools.find_packages(),
    keywords=['regression', 'tests', 'visual'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
