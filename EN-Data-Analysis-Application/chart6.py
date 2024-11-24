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

# 📦 Plotting a bar chart of best-selling and least-selling products
def draw_sales_bar_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query("SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum().sort_values()

        plt.figure(figsize=(10, 6))
        bars = plt.bar(product_sales.index, product_sales.values, color="mediumseagreen")
        plt.title("📦 Product Sales (Lowest to Highest)", fontsize=14)
        plt.xlabel("Product Name")
        plt.ylabel("Units Sold")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.3)

        for bar, value in zip(bars, product_sales.values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     str(int(value)), ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error while plotting the product sales chart: {e}")

# 🖼️ Generating a chart image for display within the dashboard
def get_sales_bar_chart_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query("SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum().sort_values()

        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(product_sales.index, product_sales.values, color="mediumseagreen")
        ax.set_title("📦 Product Sales Chart", fontsize=12)
        ax.set_xlabel("Product Name")
        ax.set_ylabel("Units Sold")
        ax.set_xticks(range(len(product_sales.index)))
        ax.set_xticklabels(product_sales.index, rotation=45, ha="right")
        ax.grid(axis="y", linestyle="--", alpha=0.3)

        for bar, value in zip(bars, product_sales.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    str(int(value)), ha="center", va="bottom", fontsize=8)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️Error while generating the product sales chart image: {e}")
        return None
