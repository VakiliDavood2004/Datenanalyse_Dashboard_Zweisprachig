# chart4.py
"""
This code uses product sales data from the sales.db database to calculate the percentage share of each 
product's sales relative to total sales, and displays the results as a pie chart. Each segment of the chart
is color-coded, and both the sales percentage and number of units sold are shown alongside each section. 
The first function displays the chart in a separate window, while the second function generates the same 
chart as a Pixmap image for display in the graphical user interface.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap