# chart6.py
"""
This code extracts product sales data from the sales.db database and calculates the total number of units sold for each 
product. It then plots a bar chart that displays products sorted from least sold to most sold, with bars colored in 
mediumseagreen. The first function displays the chart in a separate window for visual inspection, while the second 
function generates the same chart as a Pixmap image for use in the application's graphical interface or dashboard, 
including numeric labels above each bar to indicate the sales count.

"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

