# chart5.py
"""
This code retrieves sales data from the sales.db database to analyze the sales trends of different products over time. 
Transaction dates are converted to datetime format, and the data is grouped by date and product name to calculate the 
daily total sales for each item. A line chart is generated to visualize changes in sales over time, with each product 
represented by a separate line. The first function displays the chart in a standalone window, while the second function 
renders the same chart as a Pixmap image for use in the graphical user interface.
"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

