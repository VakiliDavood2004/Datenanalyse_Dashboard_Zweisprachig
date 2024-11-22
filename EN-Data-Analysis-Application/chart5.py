# chart5.py
"""
This code retrieves sales data from the sales.db database to analyze the sales trends of different products over time. 
Transaction dates are converted to datetime format, and the data is grouped by date and product name to calculate the 
daily total sales for each item. A line chart is generated to visualize changes in sales over time, with each product 
represented by a separate line. The first function displays the chart in a standalone window, while the second function 
renders the same chart as a Pixmap image for use in the graphical user interface.
"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# ⏳ Plotting the line chart of product sales over time
def draw_sales_line_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold, transaction_date FROM sales", conn)

        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df_grouped = df.groupby(["transaction_date", "product_name"])["quantity_sold"].sum().unstack().fillna(0)

        plt.figure(figsize=(10, 6))
        for column in df_grouped.columns:
            plt.plot(df_grouped.index, df_grouped[column], label=column)

        plt.title("📈 Sales Trend of Products Over Time")
        plt.xlabel("Date")
        plt.ylabel("Units Sold")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️Error while plotting the sales line chart: {e}")

# 🖼️ Generating a sales chart image for display in the dashboard
def get_sales_line_chart_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold, transaction_date FROM sales", conn)

        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df_grouped = df.groupby(["transaction_date", "product_name"])["quantity_sold"].sum().unstack().fillna(0)

        fig, ax = plt.subplots(figsize=(8, 5))
        for column in df_grouped.columns:
            ax.plot(df_grouped.index, df_grouped[column], label=column)

        ax.set_title("📈 Sales Trend of Products Over Time", fontsize=12)
        ax.set_xlabel("Date")
        ax.set_ylabel("Units Sold")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.4)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️ Error while generating the sales chart image: {e}")
        return None
