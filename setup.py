import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Degenderate",
    version="0.0.1",
    author="Daniel Clay",
    author_email="dclay.daniel@gmail.com",
    description="Semi-intelligently de-genders text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/walrus/degenderate",
    packages=setuptools.find_packages(),
    python_requires='>=3.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)