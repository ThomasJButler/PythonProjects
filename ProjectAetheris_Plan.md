# Project Aetheris - Global Climate Anomaly Detector - Development Plan

This document outlines the planned phases for developing the Project Aetheris script.

## Goal

To create a Python tool that fetches, processes, analyzes, and visualizes key global climate datasets to identify statistically significant anomalies and trends.

## Environment Setup (Anaconda)

It is recommended to use Anaconda or Miniconda to manage the Python environment and dependencies for this project.

1.  **Create Conda Environment:**
    ```bash
    conda create --name aetheris python=3.9 # Or desired Python version
    conda activate aetheris
    ```
2.  **Install Dependencies:** Dependencies will be installed using `conda install` or `pip install` within the activated environment as needed per phase (see `requirements.txt` generated in Phase 1 and updated subsequently).

## Phases

### Phase 1: Foundational Data Fetching and Visualization (GISTEMP)

*   **Objective:** Establish basic functionality by fetching and plotting a single key dataset.
*   **Tasks:**
    1.  Create project directory (`ProjectAetheris`).
    2.  Create main script file (`aetheris.py`).
    3.  Create `requirements.txt` (`pandas`, `requests`, `matplotlib`). Install using `pip install -r requirements.txt` or `conda install pandas requests matplotlib`.
    4.  Implement function to fetch NASA GISTEMP global annual mean temperature anomaly data (e.g., from `https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data/GLB.Ts+dSST.txt`).
    5.  Implement function using `pandas` to parse the fetched text data, handling comments/headers, and extracting Year and Anomaly columns.
    6.  Implement function using `matplotlib` to plot Temperature Anomaly vs. Year.
    7.  Add basic plot customizations (title, labels, grid).
    8.  Add a rolling average line (e.g., 10-year) to the plot for trend visualization.
    9.  Create a `main` function/block to orchestrate these steps.
*   **Outcome:** A working script that visualizes the global temperature anomaly trend, runnable within the `aetheris` conda environment.

### Phase 2: Incorporating Additional Datasets

*   **Objective:** Expand the script's capability to handle multiple climate indicators.
*   **Tasks:**
    1.  Identify reliable public sources/APIs for additional datasets:
        *   Atmospheric CO2 concentrations (e.g., Mauna Loa data from NOAA/ESRL).
        *   Global Mean Sea Level (e.g., satellite altimetry data from NOAA or NASA).
    2.  Update `requirements.txt` if new libraries are needed (e.g., potentially `netCDF4` or `xarray` if data is in NetCDF format). Install new dependencies.
    3.  Implement separate fetching functions for each new data source.
    4.  Implement parsing functions tailored to the format of each new dataset (CSV, JSON, NetCDF, etc.).
    5.  Adapt the main script structure to handle multiple data streams (e.g., using classes or a more modular function structure).
    6.  Add plotting functions for the new datasets, potentially allowing comparison on separate subplots or a shared timeline.
*   **Outcome:** Script can fetch, process, and visualize multiple key climate indicators.

### Phase 3: Data Alignment and Correlation Analysis

*   **Objective:** Prepare data for comparative analysis and investigate relationships between indicators.
*   **Tasks:**
    1.  Implement logic to align the different datasets onto a common time index (e.g., resampling monthly or annual means using `pandas`). Handle missing data appropriately (interpolation or dropping).
    2.  Calculate correlation coefficients between the aligned datasets (e.g., Temperature Anomaly vs. CO2).
    3.  Visualize correlations using scatter plots or a correlation heatmap (`seaborn`).
    4.  Update `requirements.txt` (add `seaborn`, `scipy` if needed for stats). Install new dependencies.
*   **Outcome:** Aligned datasets ready for analysis, with initial insights into correlations between climate variables.

### Phase 4: Basic Anomaly Detection

*   **Objective:** Implement statistical methods to identify potential anomalies in individual time series.
*   **Tasks:**
    1.  Implement anomaly detection based on standard deviations: Identify points exceeding a threshold (e.g., 2 or 3 standard deviations) from a rolling mean.
    2.  Implement anomaly detection using Z-scores.
    3.  Visualize the detected anomalies on the time-series plots (e.g., highlighting points).
    4.  Provide summary statistics about detected anomalies.
*   **Outcome:** Script can flag statistically unusual data points in each climate indicator time series.

### Phase 5: Advanced Anomaly Detection (Machine Learning)

*   **Objective:** Apply machine learning techniques for more sophisticated anomaly detection.
*   **Tasks:**
    1.  Update `requirements.txt` (add `scikit-learn`, potentially `tensorflow` or `pytorch` for advanced models). Install new dependencies.
    2.  Implement anomaly detection using algorithms like:
        *   Isolation Forest (`scikit-learn`).
        *   Local Outlier Factor (LOF) (`scikit-learn`).
        *   (Optional Advanced) LSTM Autoencoders (`tensorflow`/`pytorch`) for detecting deviations in temporal patterns.
    3.  Train models (where applicable) on historical data.
    4.  Compare results from different ML methods and statistical methods.
    5.  Refine visualization to clearly show anomalies detected by different methods.
*   **Outcome:** Enhanced anomaly detection capabilities using ML, potentially identifying more subtle deviations.

### Phase 6: Reporting and User Interface (Optional)

*   **Objective:** Improve usability and output presentation.
*   **Tasks:**
    1.  Implement functionality to generate summary reports (e.g., text files or PDFs) containing key findings, plots, and anomaly lists.
    2.  (Optional) Develop a simple command-line interface (CLI) using `argparse` to allow users to specify datasets, date ranges, or analysis methods.
    3.  (Optional Advanced) Develop a graphical user interface (GUI) using libraries like `PyQt5`, `Tkinter`, or a web framework like `Flask`/`Dash` for interactive exploration.
*   **Outcome:** More user-friendly script with options for report generation and potentially interactive use.

## Dependencies (Cumulative - Install via Conda/Pip)

*   `python>=3.8` (Recommended)
*   `pandas`
*   `requests`
*   `matplotlib`
*   `seaborn`
*   `numpy`
*   `scipy`
*   `scikit-learn`
*   `statsmodels`
*   (Potentially `xarray`, `netCDF4`)
*   (Potentially `tensorflow` or `pytorch`)
*   (Potentially `argparse`, `PyQt5`, `Flask`, `Dash`, `reportlab` for PDF reports)

This plan provides a structured approach, starting simple and adding complexity in manageable phases, using Anaconda for environment management.
