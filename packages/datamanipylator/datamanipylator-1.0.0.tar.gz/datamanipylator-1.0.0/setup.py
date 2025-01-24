from setuptools import setup, find_packages

setup(
    name="datamanipylator",
    version="1.0.0",
    author="Jose Caballero",
    author_email="jcaballero.hep@gmail.com",
    description="Library to process data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jose-caballero/manipylator",
    packages=find_packages(),  # Automatically find packages
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

