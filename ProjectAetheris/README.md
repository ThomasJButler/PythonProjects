# Project Aetheris - Climate Data Visualiser (Temp & CO2)

![Project Aetheris Top Image](/images/topimage.png "Project Aetheris")

This script fetches, processes, and visualises key climate indicators:
1.  NASA GISS Surface Temperature Analysis (GISTEMP v4) global annual mean temperature anomaly.
2.  NOAA Mauna Loa atmospheric CO2 concentration (monthly mean).

It provides plots showing the historical trends of these indicators individually and aligned together on an annual basis.

## What it Does

*   **Fetches Data:** Downloads the latest GISTEMP temperature anomaly data and Mauna Loa CO2 data from official NASA GISS and NOAA GML sources.
*   **Processes Data:** Parses the text-based data files into structured pandas DataFrames.
*   **Visualises Individually:** Generates separate plots using matplotlib for:
    *   Global temperature anomaly (°C) vs. Year (including a 10-year rolling average).
    *   Mauna Loa CO2 concentration (ppm) vs. Year.

![GISTEMP Data Visualisation](/images/GISTEMP.png "GISTEMP Temperature Anomaly")

*   **Aligns Data:** Resamples the monthly CO2 data to annual means and aligns it with the annual temperature anomaly data based on the year.
*   **Visualises Combined:** Generates a twin-axis plot showing the aligned annual temperature anomaly and CO2 concentration data on the same timeline for comparison.

![Aligned Temperature and CO2 Data](/images/AnnualMean.png "Aligned Temperature and CO2")

*   **(Note:** Sea level data fetching was attempted but removed due to difficulties finding a stable, free data source URL.)*

## Data Sources

The script fetches data from the following official URLs:

*   **GISTEMP:** `https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt`
*   **Mauna Loa CO2:** `https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt`

## Why it's Useful

*   **Climate Change Insight:** Provides direct visualisation of two primary indicators of global climate change – temperature and CO2 concentration.
*   **Correlation Visualisation:** The aligned plot helps visualise the relationship between rising CO2 levels and global temperature anomalies over time.
*   **Data Accessibility:** Makes accessing and viewing these important scientific datasets straightforward.
*   **Educational Tool:** Can be used to understand historical climate trends and the interplay between different indicators.
*   **Foundation:** Serves as the base for the larger Project Aetheris goal of analysing multiple climate indicators, detecting anomalies, and potentially making predictions.

## Setup and Usage

This project uses Python and requires a few common data science libraries. It's recommended to use Anaconda/Miniconda for environment management.

1.  **Clone the Repository (if applicable) or Download Files:**
    Ensure you have the `aetheris.py` and `requirements.txt` files in a directory named `ProjectAetheris`.

2.  **Create and Activate Conda Environment:**
    Open your terminal or Anaconda Prompt, navigate to the parent directory of `ProjectAetheris`, and run:
    ```bash
    # Create the environment (only needs to be done once)
    conda create --name aetheris python=3.9 -y 

    # Activate the environment (do this every time you open a new terminal for this project)
    conda activate aetheris
    ```

3.  **Install/Update Dependencies:**
    While the `aetheris` environment is active, navigate *into* the `ProjectAetheris` directory and install/update the required packages:
    ```bash
    cd ProjectAetheris 
    pip install -r requirements.txt
    ```
    *(Alternatively, you could use `conda install pandas requests matplotlib`)*

4.  **Run the Script:**
    Execute the script from within the `ProjectAetheris` directory:
    ```bash
    python aetheris.py
    ```
    This will fetch the data and display the plots (GISTEMP, CO2, and Aligned).

## Dependencies

*   pandas
*   requests
*   matplotlib

## Bonus: Visualising Deterministic Chaos with the Lorenz Attractor

In the `ProjectAetheris/lorenz/` directory, you'll find `lorenz_chaos.py`, a script that demonstrates a fundamental concept in chaos theory using the Lorenz system.

### What it Does

*   **Simulates the Lorenz System:** Numerically solves the three differential equations that define the Lorenz system.
*   **Visualises the Attractor:** Generates a 3D plot showcasing the iconic "butterfly" shaped Lorenz attractor.

### Why it's Useful

*   **Illustrates Chaos Theory:** Provides a visual representation of how simple, deterministic rules can lead to complex, unpredictable behaviour.
*   **Demonstrates the Butterfly Effect:** Highlights the sensitivity to initial conditions, where tiny changes can drastically alter the system's trajectory.
*   **Educational Tool:** Offers an accessible way to understand a concept that revolutionized fields like meteorology, physics, and economics.

### Setup and Usage

1.  **Ensure Dependencies are Installed:** The `numpy` and `matplotlib` libraries are required. If you've followed the setup for Project Aetheris, these are already installed in your `aetheris` environment. Otherwise, create a new environment or install them in your existing environment.
2.  **Navigate to the `lorenz/` Directory:**
    ```bash
    cd ProjectAetheris/lorenz
    ```
3.  **Run the Script:**
    Execute the script:
    ```bash
    python lorenz_chaos.py
    ```
    The script will simulate the Lorenz system and display the 3D plot. Close the plot window to exit.
