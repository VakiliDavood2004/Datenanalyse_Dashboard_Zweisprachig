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

def generate_summary():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        row_count = len(df)
        total_purchase = df["total_purchase"].sum()
        total_sale = df["total_sale"].sum()
        profit = total_sale - total_purchase
        unique_products = df["product_code"].nunique()
        max_sale_qty = df["quantity_sold"].max()
        min_sale_qty = df["quantity_sold"].min()

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        product_values = df.groupby("product_name")["total_sale"].sum()

        report_lines = [
            f"📊 General Inventory Report: ",
            f"- Number of Records: {row_count}",
            f"- Number of distinct items: {unique_products}",
            f"- Total purchase amount: {total_purchase:,.0f} Dollars",
            f"- Total sales amount: {total_sale:,.0f} Dollars",
            f"- Total profit: {profit:,.0f} Dollars",
            f"- Highest sales volume: {max_sale_qty}",
            f"- Lowest sales volume: {min_sale_qty}",
            "",
            f"🔹 Sales by product:"
        ]

        for product in product_sales.index:
            qty = product_sales[product]
            value = product_values[product]
            report_lines.append(f"  • {product}: {qty} Quantity, Total Sales Amount: {value:,.0f} Dollars")

        return "\n".join(report_lines)

    except Exception as e:
        return f"⚠️ Error generating report: {e}"
