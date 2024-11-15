# chart2.py
"""
This code uses data from the sales.db database to calculate the profit of products that have generated positive returns. 
It then creates a pie chart representing the relative share of each product's profit. 
Green segments indicate profitable products, and percentage labels are displayed on each section of the chart. 
The first function displays the chart in a separate window, while the second function generates the same 
chart as a Pixmap image for use in the graphical user interface.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

