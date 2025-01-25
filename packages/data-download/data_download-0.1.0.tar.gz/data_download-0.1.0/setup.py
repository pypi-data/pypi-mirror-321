from setuptools import setup, find_packages

setup(
    name="data-download",
    version="0.1.0",
    description="Download ERA5 data from Copernicus API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sididk Barbhuiya",
    author_email="siddikbarbhuiya@gmail.com",
    url="https://github.com/himpactlab/Data_download",
    packages=find_packages(),
    install_requires=[
        "cdsapi",
        "xarray",
        "netCDF4"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
