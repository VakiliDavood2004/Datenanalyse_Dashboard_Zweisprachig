# chart3.py
"""
This code reads data from the sales.db database to calculate the remaining inventory of each product 
(by subtracting the number of sales from the number of purchases), and then generates a bar chart 
showing product stock levels. The first function displays the chart in a separate window, allowing 
users to visually inspect the remaining quantity of each item. The second function renders the same 
chart as a Pixmap image for use in the graphical user interface. All bars are drawn in dodgerblue color, 
with numeric labels displayed above each bar.
"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📉 Plotting the remaining inventory chart in a separate window
def draw_inventory_bar_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_purchased, quantity_sold FROM sales", conn)

        df["inventory"] = df["quantity_purchased"] - df["quantity_sold"]
        product_inventory = df.groupby("product_name")["inventory"].sum().sort_values()

        plt.figure(figsize=(10, 5))
        bars = plt.bar(product_inventory.index, product_inventory.values, color="dodgerblue")
        plt.title("📦 Remaining Inventory of Each Product")
        plt.xlabel("Product Name")
        plt.ylabel("Remaining Inventory Count")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.4)

        for bar, value in zip(bars, product_inventory.values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     str(int(value)), ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error while plotting the inventory chart: {e}")

# 🖼️ Converting the inventory chart to an image for display within the dashboard
def get_inventory_chart_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_purchased, quantity_sold FROM sales", conn)

        df["inventory"] = df["quantity_purchased"] - df["quantity_sold"]
        product_inventory = df.groupby("product_name")["inventory"].sum().sort_values()

        fig, ax = plt.subplots(figsize=(8, 4.5))
        bars = ax.bar(product_inventory.index, product_inventory.values, color="dodgerblue")
        ax.set_title("📦 Remaining Inventory of Each Product", fontsize=12)
        ax.set_xlabel("Product Name")
        ax.set_ylabel("Remaining Inventory Count")
        ax.set_xticks(range(len(product_inventory.index)))
        ax.set_xticklabels(product_inventory.index, rotation=45, ha="right")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        for bar, value in zip(bars, product_inventory.values):
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
        print(f"⚠️ Error while generating the inventory chart image: {e}")
        return None
