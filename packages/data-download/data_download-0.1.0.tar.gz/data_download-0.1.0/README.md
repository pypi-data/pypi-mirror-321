# ERA5 Data Downloader

This Python package provides functionality to download **ERA5 reanalysis data** from the **Copernicus Climate Data Store (CDS)**. The package includes a robust system to handle retries, verify the integrity of NetCDF files, and log all operations for easy troubleshooting.

---

## Features

- Downloads ERA5 variables for a specified geographical area and time range.
- Supports:
  - `2m_temperature`
  - `10m_u_component_of_wind`
  - `10m_v_component_of_wind`
  - `total_precipitation`
  - Additional variables can be added easily.
- Automatically verifies the integrity of downloaded NetCDF files.
- Configurable retry mechanism for failed downloads.
- Detailed logging for debugging and monitoring.

---

## Installation

### Prerequisites

1. **Python**: Ensure you have Python 3.6 or above installed.
2. **Required Libraries**:
   Install the required dependencies using:
   ```bash
   pip install -r requirements.txt

# ERA5 Data Downloader

This Python package provides functionality to download **ERA5 reanalysis data** from the **Copernicus Climate Data Store (CDS)**. The package includes a robust system to handle retries, verify the integrity of NetCDF files, and log all operations for easy troubleshooting.

---

## **Required Dependencies**

The script uses the following Python libraries:

- **`cdsapi`**: For interacting with the Copernicus Climate Data Store API.
- **`xarray`**: For working with NetCDF files.
- **`logging`**: For detailed logging.
- **`netCDF4`**: For handling NetCDF files.

---

## **Configuration**

### **CDS API Key**

To use the `cdsapi` package, you must configure your CDS API key. Follow these steps:

1. Open your terminal and create a `.cdsapirc` file in your home directory:
   ```bash
   nano ~/.cdsapirc
