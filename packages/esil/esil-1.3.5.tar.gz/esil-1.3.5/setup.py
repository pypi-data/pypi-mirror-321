from setuptools import setup, find_packages

setup(
    name="esil",
    version="1.3.5",
    author="Devin Long",
    author_email="long.sc@qq.com",
    description="commonly used functions written by Devin Long",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Devin-Long-7/esil",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "pandas",
        "xarray",
        "scipy",
        "tqdm",
        "netCDF4",
        "pyproj",
        "SQLAlchemy",
        "chardet",
        "sympy",
        "shapely",
        "pytz",
        # "pykrige",
        # "matplotlib<3.9,>=1.5",  # Basemap 要求的 Matplotlib 版本为小于3.9且大于等于1.5
        "cartopy",
        "geopandas",
    ],
)
