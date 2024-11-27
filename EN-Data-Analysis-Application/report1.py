# report1.py
"""
This function generates a summary report using the data stored in the sales.db database. It extracts information such 
as the number of records, the number of distinct products, total purchases and sales, total profit, and the highest and 
lowest sales quantities. Then, for each product, it calculates the total sales quantity and the total sales value, and 
returns a structured textual report. If an error occurs during execution, an appropriate error message will be returned 
as a string.

"""


import sqlite3
import pandas as pd
import numpy as np
