import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(left=1850, right=2075)
    ax.set_ylim(bottom=-1,top=17)


    # Create first line of best fit
    linreg_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    l1_xdata = np.linspace(1880, 2051, 172)
    l1_ydata = np.linspace(1880 * linreg_1.slope + linreg_1.intercept, linreg_1.slope * 2051 + linreg_1.intercept, 172)
    ax.add_line(plt.Line2D(l1_xdata, l1_ydata))
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    linreg_2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    l2_xdata = np.linspace(2000, 2051, 51)
    l2_ydata = np.linspace(2000 *linreg_2.slope + linreg_2.intercept, linreg_2.slope * 2051 + linreg_2.intercept, 51)
    ax.add_line(plt.Line2D(l2_xdata, l2_ydata))

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.plot(df['Year'], df['CSIRO Adjusted Sea Level'], 'wo', markersize=2)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()