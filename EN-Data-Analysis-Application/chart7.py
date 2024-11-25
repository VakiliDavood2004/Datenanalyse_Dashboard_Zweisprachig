# chart7.py
"""
This code extracts the number of sales for each product from the sales.db database and displays each product’s 
share of total sales as a pie chart. If no sales are recorded, a warning message is printed. In the chart, each 
product is represented with a distinct color, and both the percentage share and the numerical count are shown. 
The first function displays the chart in a separate window, while the second function generates the same chart 
as a Pixmap image for use in the graphical interface.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap
