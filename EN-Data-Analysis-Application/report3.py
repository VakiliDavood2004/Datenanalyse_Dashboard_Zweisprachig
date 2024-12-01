# report3.py
"""
This function retrieves sales data from the sales.db database and enables temporal analysis by converting transaction 
dates into datetime format. Rows lacking valid dates are removed first. Then, purchase and sales data are grouped and 
aggregated on a daily and monthly basis. The peak sales day is identified, and reports are generated for monthly sales 
trends and product performance by month. Finally, a textual report is produced, including the highest sales day, monthly 
trends, and product performance for each month. If an error occurs, an appropriate warning message will be returned.

"""


import sqlite3
import pandas as pd
import numpy as np

