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

# 📊 Displaying the product profit pie chart in a separate window
def draw_profit_pie_chart():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT product_name, total_purchase, total_sale FROM sales", conn)
        conn.close()

        df["profit"] = df["total_sale"] - df["total_purchase"]
        product_profit = df.groupby("product_name")["profit"].sum()
        positive = product_profit[product_profit > 0]

        if positive.empty:
            print("⚠️ There are no profitable products to display in the chart.")
            return

        labels = positive.index
        values = positive.values
        colors = ["green"] * len(positive)

        plt.figure(figsize=(8, 6))
        plt.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*sum(values)):,} $)",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        plt.title("Relative Profit Share of Products", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error while plotting the profit pie chart: {e}")

# 🖼️ Generating a chart image for display within the main page
def get_profit_pie_pixmap():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT product_name, total_purchase, total_sale FROM sales", conn)
        conn.close()

        df["profit"] = df["total_sale"] - df["total_purchase"]
        product_profit = df.groupby("product_name")["profit"].sum()
        positive = product_profit[product_profit > 0]

        if positive.empty:
            return None

        labels = positive.index
        values = positive.values
        colors = ["green"] * len(positive)

        fig, ax = plt.subplots(figsize=(6.5, 5))
        ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title("Relative Profit Share of Products", fontsize=12)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️ Error while generating the profit pie chart image: {e}")
        return None
