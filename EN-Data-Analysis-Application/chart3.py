# chart3.py
"""
This code reads data from the sales.db database to calculate the remaining inventory of each product 
(by subtracting the number of sales from the number of purchases), and then generates a bar chart 
showing product stock levels. The first function displays the chart in a separate window, allowing 
users to visually inspect the remaining quantity of each item. The second function renders the same 
chart as a Pixmap image for use in the graphical user interface. All bars are drawn in dodgerblue color, 
with numeric labels displayed above each bar.
"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap