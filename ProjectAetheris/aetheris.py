# Project Aetheris - Phase 1: GISTEMP Data Visualization
# Fetches, parses, and plots NASA GISTEMP global annual mean temperature anomaly data.

import requests
import pandas as pd
import matplotlib.pyplot as plt
import io # Needed for reading string data into pandas
# Removed BeautifulSoup and urljoin

# --- Configuration ---
GISTEMP_URL = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt"
CO2_URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt" # Monthly Mauna Loa CO2
# SEA_LEVEL_URL removed due to unstable links
ROLLING_AVG_WINDOW = 10 # Years for rolling average

# --- Data Fetching ---
def fetch_data(url, data_name):
    """Fetches data from the specified URL, including a User-Agent header."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes
        print(f"Successfully fetched {data_name} data from {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {data_name} data from {url}: {e}")
        return None

def fetch_gistemp_data(url):
    """DEPRECATED: Use fetch_data instead."""
    return fetch_data(url, "GISTEMP")

# Removed find_sea_level_file_url function

# --- Data Processing ---
def parse_gistemp_data(data_text):
    """Parses the GISTEMP text data into a pandas DataFrame."""
    if data_text is None:
        return None

    # Find the start of the data section (look for lines starting with a year)
    lines = data_text.splitlines()
    data_start_line = 0
    for i, line in enumerate(lines):
        if line.strip().startswith(('1', '2')): # Assumes years start with 1 or 2
             # Check if the first element looks like a year and the second a number
            parts = line.split()
            if len(parts) >= 2 and parts[0].isdigit() and len(parts[0]) == 4:
                 try:
                     float(parts[1]) # Check if second part is numeric
                     data_start_line = i
                     break
                 except ValueError:
                     continue # Not the data line yet

    if data_start_line == 0:
        print("Error: Could not find the start of the data section in the fetched text.")
        return None

    # Read the data section, skipping metadata/comments
    # Use io.StringIO to treat the relevant part of the string as a file
    data_io = io.StringIO('\n'.join(lines[data_start_line:]))

    try:
        # Read data, using regex for whitespace separation, use first two columns
        df = pd.read_csv(data_io, sep='\s+', usecols=[0, 1], names=['Year', 'Anomaly'], header=None)
        # Ensure data types are correct
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df['Anomaly'] = pd.to_numeric(df['Anomaly'], errors='coerce')
        df = df.dropna() # Drop rows where conversion failed
        df = df.set_index('Year') # Set Year as index
        print("Successfully parsed data.")
        return df
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

def parse_co2_data(data_text):
    """Parses the Mauna Loa CO2 text data into a pandas DataFrame."""
    if data_text is None:
        return None

    # Find the start of the actual data by skipping comment lines
    lines = data_text.splitlines()
    data_lines = [line for line in lines if not line.strip().startswith('#')]

    if not data_lines:
        print("Error: No data lines found after skipping comments in CO2 data.")
        return None

    # Use io.StringIO to treat the relevant part of the string as a file
    data_io = io.StringIO('\n'.join(data_lines))

    try:
        # Columns in the file are typically: year, month, decimal date, average, interpolated, trend, #days
        # We need year, month, and average (column index 3)
        df = pd.read_csv(data_io, sep='\s+', usecols=[0, 1, 3], names=['Year', 'Month', 'CO2_ppm'], header=None)

        # Create a datetime index from Year and Month
        # Handle potential errors during datetime conversion
        df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1), errors='coerce')
        df = df.dropna(subset=['Date']) # Drop rows where date conversion failed
        df = df.set_index('Date')
        df = df.drop(columns=['Year', 'Month']) # Keep only CO2_ppm

        # Convert CO2_ppm to numeric, coercing errors (like -99.99 for missing data)
        df['CO2_ppm'] = pd.to_numeric(df['CO2_ppm'], errors='coerce')
        df = df.dropna() # Drop rows with missing CO2 data

        print("Successfully parsed Mauna Loa CO2 data.")
        return df
    except Exception as e:
        print(f"Error parsing CO2 data: {e}")
        return None

# Removed parse_sea_level_data function

# --- Data Analysis ---
def calculate_rolling_average(df, window):
    """Calculates the rolling average for the 'Anomaly' column."""
    if df is None or 'Anomaly' not in df.columns:
        return None
    col_name = f'{window}yr_Avg_Anomaly'
    df[col_name] = df['Anomaly'].rolling(window=window, center=True).mean()
    return df

def align_data(df_temp, df_co2):
    """Aligns temperature (annual) and CO2 (monthly) data to a common annual frequency."""
    if df_temp is None or df_co2 is None:
        print("Error: Cannot align data, one or both DataFrames are missing.")
        return None

    try:
        # Resample CO2 data to annual mean. Use the mean of the monthly values for each year.
        # Ensure the index is datetime first if it's not already
        if not isinstance(df_co2.index, pd.DatetimeIndex):
             df_co2.index = pd.to_datetime(df_co2.index)
        df_co2_annual = df_co2.resample('A').mean() # 'A' stands for year-end frequency

        # Extract the year from the resampled CO2 index to match the GISTEMP index (which is just the year integer)
        df_co2_annual.index = df_co2_annual.index.year
        df_co2_annual.index.name = 'Year' # Match index name

        # Join the two dataframes on their common 'Year' index
        # Use an inner join to keep only years where both datasets have data
        df_aligned = df_temp.join(df_co2_annual, how='inner')

        print(f"Successfully aligned data from {df_aligned.index.min()} to {df_aligned.index.max()}.")
        return df_aligned

    except Exception as e:
        print(f"Error aligning data: {e}")
        return None

# --- Visualization ---
def plot_temperature_anomaly(df):
    """Plots the temperature anomaly and rolling average."""
    if df is None:
        print("No data available to plot.")
        return

    rolling_avg_col = f'{ROLLING_AVG_WINDOW}yr_Avg_Anomaly'

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Anomaly'], label='Annual Anomaly', marker='.', linestyle='-', markersize=4, alpha=0.7)

    if rolling_avg_col in df.columns:
        plt.plot(df.index, df[rolling_avg_col], label=f'{ROLLING_AVG_WINDOW}-Year Rolling Average', color='red', linewidth=2)

    plt.title('Global Land-Ocean Temperature Index (GISTEMP v4)')
    plt.xlabel('Year')
    plt.ylabel('Temperature Anomaly (°C)')
    plt.axhline(0, color='grey', linestyle='--', linewidth=0.8) # Add line for 0 anomaly
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    print("Plot displayed.")

def plot_co2_data(df):
    """Plots the CO2 concentration over time."""
    if df is None or df.empty:
        print("No CO2 data available to plot.")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['CO2_ppm'], label='Monthly Mean CO2 (ppm)', color='green', linewidth=1.5)
    plt.title('Mauna Loa Atmospheric CO2 Concentration')
    plt.xlabel('Year')
    plt.ylabel('CO2 Concentration (ppm)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    print("CO2 plot displayed.")

# Removed plot_sea_level_data function

def plot_aligned_data(df):
    """Plots aligned Temperature Anomaly and CO2 data on the same figure with twin axes."""
    if df is None or df.empty:
        print("No aligned data available to plot.")
        return
    if 'Anomaly' not in df.columns or 'CO2_ppm' not in df.columns:
        print("Error: Aligned DataFrame missing required 'Anomaly' or 'CO2_ppm' columns.")
        return

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = 'tab:red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Temperature Anomaly (°C)', color=color1)
    ax1.plot(df.index, df['Anomaly'], color=color1, label='Temp Anomaly (°C)', marker='.', linestyle='-', markersize=4)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.axhline(0, color='grey', linestyle='--', linewidth=0.8) # Zero anomaly line

    # Instantiate a second axes that shares the same x-axis
    ax2 = ax1.twinx()
    color2 = 'tab:blue'
    ax2.set_ylabel('CO2 Concentration (ppm)', color=color2)
    ax2.plot(df.index, df['CO2_ppm'], color=color2, label='CO2 (ppm)', marker='.', linestyle='-', markersize=4)
    ax2.tick_params(axis='y', labelcolor=color2)

    # Add combined legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.title('Global Temperature Anomaly vs. Mauna Loa CO2 Concentration (Annual Mean)')
    fig.tight_layout() # Otherwise the right y-label is slightly clipped
    plt.show()
    print("Aligned data plot displayed.")


# --- Main Execution ---
def main():
    """Main function to run the data fetching, processing, and plotting."""
    print("--- Project Aetheris v1 ---")
    # Fetch GISTEMP Data
    gistemp_text = fetch_data(GISTEMP_URL, "GISTEMP")
    df_gistemp = parse_gistemp_data(gistemp_text)
    df_gistemp_with_avg = calculate_rolling_average(df_gistemp, ROLLING_AVG_WINDOW)
    plot_temperature_anomaly(df_gistemp_with_avg)

    # Fetch CO2 Data
    co2_text = fetch_data(CO2_URL, "Mauna Loa CO2")
    df_co2 = parse_co2_data(co2_text)
    # plot_co2_data(df_co2) # Optionally skip individual plot if aligned plot is sufficient

    # Align Data
    df_aligned = align_data(df_gistemp, df_co2)

    # Plot Aligned Data
    plot_aligned_data(df_aligned)

    # Sea level fetching removed for now due to unstable URLs
    print("Skipping sea level analysis due to difficulty finding a stable data source URL.")

    print("--- Analysis Complete ---")

if __name__ == "__main__":
    main()
