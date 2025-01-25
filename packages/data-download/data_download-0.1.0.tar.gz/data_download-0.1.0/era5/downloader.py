import cdsapi
import os
import calendar
import time
import logging
from .validator import is_valid_netcdf

# Initialize CDS API client with a timeout
try:
    client = cdsapi.Client(timeout=600)
    logging.info("CDS API client initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize CDS API client: {e}")
    raise

def download_era5_variable(variable, dataset, area, base_dir, start_year, end_year, retries=3):
    """
    Downloads ERA5 variables for a specified time range and area.

    Args:
        variable (str): The variable to download (e.g., "2m_temperature").
        dataset (str): The ERA5 dataset to use (e.g., "reanalysis-era5-land").
        area (list): The geographical area [N, W, S, E] (e.g., [38, 67, 5, 98]).
        base_dir (str): The base directory to save downloaded files.
        start_year (int): The starting year.
        end_year (int): The ending year.
        retries (int): Number of retries for failed downloads.
    """
    logging.info(f"Processing variable: {variable}")
    print(f"\nProcessing variable: {variable}")

    # Create a folder for the variable
    variable_dir = os.path.join(base_dir, variable)
    os.makedirs(variable_dir, exist_ok=True)
    logging.debug(f"Ensured directory exists: {variable_dir}")

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            # Determine the number of days in the month
            _, days_in_month = calendar.monthrange(year, month)

            # Format the month and day strings
            month_str = f"{month:02d}"
            days = [f"{day:02d}" for day in range(1, days_in_month + 1)]

            # Define the request parameters
            request = {
                "variable": [variable],
                "year": str(year),
                "month": month_str,
                "day": days,
                "time": [
                    "00:00", "01:00", "02:00",
                    "03:00", "04:00", "05:00",
                    "06:00", "07:00", "08:00",
                    "09:00", "10:00", "11:00",
                    "12:00", "13:00", "14:00",
                    "15:00", "16:00", "17:00",
                    "18:00", "19:00", "20:00",
                    "21:00", "22:00", "23:00"
                ],
                "format": "netcdf",
                "area": area,
            }

            # Define the output file path
            output_file = os.path.join(
                variable_dir, f"{variable}_{year}_{month_str}.nc"
            )
            logging.debug(f"Output file path: {output_file}")

            # Check if the file already exists
            if os.path.exists(output_file):
                logging.info(f"File already exists: {output_file}")
                print(f"\nFile already exists: {output_file}")

                # Verify if the existing file is a valid NetCDF file
                if is_valid_netcdf(output_file):
                    logging.info(f"Verified: {output_file} is a valid NetCDF file. Skipping download.")
                    print(f"Verified: {output_file} is a valid NetCDF file. Skipping download.")
                    continue  # Skip to the next file
                else:
                    logging.warning(f"Corrupted or incomplete file detected: {output_file}. Deleting and re-downloading.")
                    print(f"Corrupted or incomplete file detected: {output_file}. Deleting and re-downloading.")
                    os.remove(output_file)  # Remove the corrupted file

            # Retry logic for failed downloads
            for attempt in range(retries):
                try:
                    logging.info(f"Downloading {variable} for {year}-{month_str} (Attempt {attempt + 1})")
                    print(f"\nDownloading {variable} for {year}-{month_str} (Attempt {attempt + 1})...")
                    client.retrieve(dataset, request, output_file)
                    logging.info(f"Download initiated for {output_file}")

                    # Verify the downloaded file
                    if is_valid_netcdf(output_file):
                        logging.info(f"Successfully downloaded and verified: {output_file}")
                        print(f"Successfully downloaded and verified: {output_file}")
                        break  # Exit retry loop on success
                    else:
                        logging.error(f"Downloaded file is corrupted: {output_file}")
                        print(f"Downloaded file is corrupted: {output_file}")
                        if attempt < retries - 1:
                            logging.info("Retrying download after 10 seconds...")
                            print("Retrying download after 10 seconds...")
                            time.sleep(10)  # Wait before retrying
                        else:
                            logging.error(f"Failed to download a valid file for {variable} {year}-{month_str} after {retries} attempts.")
                            print(f"Failed to download a valid file for {variable} {year}-{month_str} after {retries} attempts.")
                except Exception as e:
                    logging.error(f"Error downloading {variable} for {year}-{month_str}: {e}")
                    print(f"Error downloading {variable} for {year}-{month_str}: {e}")
                    if attempt < retries - 1:
                        logging.info("Retrying download after 10 seconds...")
                        print("Retrying download after 10 seconds...")
                        time.sleep(10)  # Wait before retrying
                    else:
                        logging.error(f"Failed to download {variable} for {year}-{month_str} after {retries} attempts.")
                        print(f"Failed to download {variable} for {year}-{month_str} after {retries} attempts.")
