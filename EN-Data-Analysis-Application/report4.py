# report4.py
"""
This function reads product sales and purchase data from the sales.db database and provides a comprehensive analysis of 
inventory status. For each product, profit amount and sales percentage relative to purchase quantity are calculated.  
Then, the data is grouped by product to derive the average purchase price, highest sales price, total profit, and sales 
percentage. High-selling, low-selling, high-profit, and low-profit products are identified. A textual report is generated,
including sales percentages, pricing impact, and classification of weak and strong products in terms of sales and profitability.  
If an error occurs, an appropriate message will be returned.

"""


import sqlite3
import pandas as pd
import numpy as np