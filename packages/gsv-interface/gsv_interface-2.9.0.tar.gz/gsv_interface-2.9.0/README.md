# GSV interface
A tool for accessing the GSV data from `FDB` and converting it into `xarray`.


## Core idea
The current approach can be summarized in three steps:

 1. Use `pyfdb` to request data from the `FDB`. This will return a `pyfdb.Dataretriever` file-like object from which you can read all GRIB messages matching a given request.

 2. Use `eccodes-python` to decode the necessary information of each GRIB message (data, coordinates, attributes...). A custom iterator (`MessageIterator`) is  used to iterate over each message in the `pyfdb.DataRetriever` object.

 3. If requested by the user, interpolate the result to a regular LonLat grid of choice.

All requested messages are packed in a single `xarray.Dataset` object and returned to the user.

## Installation instructionss
The `gsv-interface` package is available to install through pip. It can be installed with the folloeing command:

```
pip install gsv-interface
```

## Checking installation
Top check the installation was succesfull run Python and try to import `gsv`.
```
>>> import gsv
>>> gsv.__version__
```
This should print the version number of the chosen release.

 ## Dependencies
The followin non-Python libraries are required:
 - ecCodes: https://github.com/ecmwf/eccodes
 - fdb: https://github.com/ecmwf/fdb


 This tool depends on the following Python modules, which are automatically installed though `pip`.

  - "pyfdb==0.1.1",
  - "numpy",
  - "xarray",
  - "eccodes",
  - "healpy",
  - "dask",
  - "netcdf4",
  - "cfgrib",
  - "sparse",
  - "cdo",
  - "smmregrid==0.1.0",
  - "polytope-client",
  - "pyyaml",
  - "jinja2",
