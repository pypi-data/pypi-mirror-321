# Macroecon-Tools
A open-source set of tools to assist with macroeconomic work. The package includes two classes, `Timeseries` and `TimeseriesTable`, for working with time series data and collections of time series. The package is built on `pandas` and `numpy` to offer additional metadata and advanced operations tailored for macroeconomic analysis of time series.

---

# Modules
- `timeseries`: Contains the datastructures extended from pd.Series and pd.DataFrame.
    - `Timeseries`: A class that extends pd.Series to include metadata and additional methods.
    - `TimeseriesTable`: A class that extends a dictionary and includes functionality from pd.DataFrame.
- `fetch_data`: Contains functions to fetch data from the internet.
    - `get_fred`: Fetches data from the Federal Reserve Economic Data (FRED) API.
    - `get_barnichon`: Fetches and parses data from the Barnichon dataset.
    - `get_ludvigson`: Fetches and parses data from the Ludvigson dataset.
- `visualizer`: Contains functions to visualize time series data.
    - `vis_multi_series`: Visualizes multiple time series on the same plot.

# Installation
To install the package, run the following command in the terminal:
```bash
pip install macroecon-tools
```

---

# Timeseries Module
## Timeseries Class
The `Timeseries` class extends the `pd.Series` class to include metadata and additional methods. The class is initialized with a `pd.Series` object and additional metadata. The metadata includes the following:
- `name`: The name of the time series.
