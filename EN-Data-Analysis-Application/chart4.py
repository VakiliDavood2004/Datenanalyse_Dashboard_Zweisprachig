# chart4.py
"""
This code uses product sales data from the sales.db database to calculate the percentage share of each 
product's sales relative to total sales, and displays the results as a pie chart. Each segment of the chart
is color-coded, and both the sales percentage and number of units sold are shown alongside each section. 
The first function displays the chart in a separate window, while the second function generates the same 
chart as a Pixmap image for display in the graphical user interface.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📊 Plotting the pie chart of each product's sales percentage
def draw_sold_percentage_pie_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        total_sold = product_sales.sum()

        if total_sold == 0:
            print("⚠️ No sales have been recorded.")
            return

        labels = product_sales.index
        values = product_sales.values
        colors = plt.cm.Paired.colors[:len(labels)]

        plt.figure(figsize=(8, 6))
        plt.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*total_sold)} units)",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        plt.title("Percentage of Each Product's Sales from Total Sales", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error while plotting the sales pie chart: {e}")

# 🖼️ Generating a chart image for display in the dashboard
def get_sold_percentage_pie_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        total_sold = product_sales.sum()

        if total_sold == 0:
            return None

        labels = product_sales.index
        values = product_sales.values
        colors = plt.cm.Paired.colors[:len(labels)]

        fig, ax = plt.subplots(figsize=(6.5, 5))
        ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title("Sales Percentage of Each Product" , fontsize=12)

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
