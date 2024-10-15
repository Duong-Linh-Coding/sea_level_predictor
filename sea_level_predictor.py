import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    
    # Create first line of best fit
    res = linregress(x,y)
    x_pred = pd.Series(i for i in range(1880,2051))
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred,y_pred,"r")

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res2 = linregress(new_x,new_y)
    new_x_pred = pd.Series(i for i in range(2000,2051))
    new_y_pred = res2.slope*new_x_pred + res2.intercept
    plt.plot(new_x_pred,new_y_pred,"g")
    
    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()