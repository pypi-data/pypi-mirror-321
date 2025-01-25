import xarray as xr
import logging

def is_valid_netcdf(file_path):
    """
    Verifies the integrity of a NetCDF file.

    Args:
        file_path (str): Path to the NetCDF file.

    Returns:
        bool: True if the file is valid, False otherwise.
    """
    try:
        logging.debug(f"Verifying NetCDF file: {file_path}")
        ds = xr.open_dataset(file_path)
        ds.close()
        logging.debug(f"Verification successful for {file_path}")
        return True
    except Exception as e:
        logging.error(f"File verification failed for {file_path}: {e}")
        return False
