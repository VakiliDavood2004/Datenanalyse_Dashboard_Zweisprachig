# report2.py
"""
This function retrieves data from the sales.db database and calculates the total profit and profitability percentage 
for each product. First, the numeric and percentage profit are computed for each row. Then, the data is grouped by 
product name to obtain the total purchase amount, total sales amount, total profit, and profit percentage for each 
product. Products are sorted by total profit to identify the most profitable and least profitable items. Next, a textual 
report is generated, including the top 3 products with the highest profit, the bottom 3 products with the lowest profit, 
and a complete ranking of all products based on profitability. If an error occurs, an appropriate error message will be 
returned.

"""


import sqlite3
import pandas as pd
import numpy as np