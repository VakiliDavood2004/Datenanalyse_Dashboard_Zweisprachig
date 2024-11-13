# chart.py
"""
This code uses pandas and matplotlib to analyze product profitability from the sales.db database. 
It first reads the purchase and sales data of products and calculates the profit for each item. 
A bar chart is then plotted to visualize profitability: 
products with positive profit are shown in green, and those with negative profit in red. 
In the first function, the chart is displayed in a separate window. 
In the second function, the chart is rendered as a Pixmap image for use in the graphical user interface.

"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📉 Rendering the chart in an independent window
def draw_profit_bar_chart():
    try:
        conn = sqlite3.connect("sales.db")
        query = "SELECT product_name, total_purchase, total_sale FROM sales"
        df = pd.read_sql_query(query, conn)
        conn.close()

        df["profit"] = df["total_sale"] - df["total_purchase"]
        product_profit = df.groupby("product_name")["profit"].sum().sort_values()
        colors = ["green" if p >= 0 else "red" for p in product_profit]

        plt.figure(figsize=(10, 5))
        bars = plt.bar(product_profit.index, product_profit.values, color=colors)
        plt.title("📉 Product Profitability Chart")
        plt.xlabel("Product Name")
        plt.ylabel("Total Profit (Toman)")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.5)

        for bar, value in zip(bars, product_profit.values):
            y = bar.get_height()
            offset = 20000 if y >= 0 else -20000
            plt.text(bar.get_x() + bar.get_width() / 2, y + offset,
                     f"{int(value):,}", ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error while plotting the profitability chart: {e}")

