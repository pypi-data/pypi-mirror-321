# Description: a visulization module for timeseries data

# Import visualization libraries
import matplotlib.pyplot as plt

# Add path to current directory
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import timeseries datastructures
from timeseries import Timeseries, TimeseriesTable

# Function to plot multiple timeseries in one graph 
def vis_multi_series(data: TimeseriesTable, save_path: str, variables: dict[str, str] = {}, start_date: str = "", end_date: str = "", is_percent: bool = False):
    """
    Creates a plot of multiple timeseries data in one graph with the data and variables provided.

    Parameters
    ----------
    data : TimeseriesTable
        The timeseries data to be plotted.
    save_path : str
        The path to save the plot, also indicates the type of file to save as (supports pdf, png, eps, etc.)
    variables : dict[str, str], optional
        A dictionary containing the variable name and the title of the plot. 
        Default: {} (indicates all variables in the TimeseriesTable will be plotted).
    start_date : str, optional
        The start date of the plot.
        Default: "" (indicates the start date of the data).
    end_date : str, optional
        The end date of the plot. 
        Default: "" (indicates the end date of the data).
    is_percent : bool, optional
        Indicates if the y-axis is in percentage format.
        Default: False (indicates the y-axis is not in percentage format).

    Notes
    -----
    The plot will be saved to the path specified in the save_path parameter.
    """
    # Check for variables
    if len(variables) == 0:
        for var in data:
            variables[var] = var
    # Map variables to list
    variables = [(var, variables[var]) for var in variables]
    # Create a figure and axis
    fig, axs = plt.subplots(len(variables), figsize=(6.5, 4))
    # Plot variables
    for idx, ax in enumerate(axs.flat):
        # plot data
        ax.plot(data.df[variables[idx][0]][start_date:end_date])
        # set title
        ax.set_title(variables[idx][1])
        # set y-axis format
        if is_percent:
            ax.yaxis.set_major_formatter('{x:.0f}%')
        else:
            ax.yaxis.set_major_formatter('{x:.0f}')
        # format graph
        ax.grid()
        ax.autoscale(tight=True)
        ax.label_outer()

    # Use tight layout
    plt.tight_layout()
    # Add 5% padding to each y-axis
    for idx, ax in enumerate(axs.flat):
        ax.margins(y=0.05)

    # Save plot
    plt.savefig(save_path)
    # Close plot
    plt.close()