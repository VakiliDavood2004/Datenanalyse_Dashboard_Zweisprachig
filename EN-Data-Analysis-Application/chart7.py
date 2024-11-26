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

# 🎯 Plotting a pie chart of each product's sales share
def draw_sales_share_pie_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query("SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        total_sold = product_sales.sum()

        if total_sold == 0:
            print("⚠️ No sales have been recorded.")
            return

        labels = product_sales.index
        values = product_sales.values
        colors = plt.cm.tab20.colors[:len(labels)]

        plt.figure(figsize=(8, 6))
        plt.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*total_sold)} units)",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        plt.title("🥧 Share of Total Sales per Product", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error generating the sales share chart: {e}")

# 🖼️ Generating chart image for display in the dashboard
def get_sales_share_pie_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query("SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        total_sold = product_sales.sum()

        if total_sold == 0:
            return None

        labels = product_sales.index
        values = product_sales.values
        colors = plt.cm.tab20.colors[:len(labels)]

        fig, ax = plt.subplots(figsize=(6.5, 5))
        ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title("🥧 Sales Share of Each Product", fontsize=12)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️ Error generating sales share image: {e}")
        return None
