# report2.py
"""
This function retrieves data from the sales.db database and calculates the total profit and profitability percentage 
for each product. First, the numeric and percentage profit are computed for each row. Then, the data is grouped by 
product name to obtain the total purchase amount, total sales amount, total profit, and profit percentage for each 
product. Products are sorted by total profit to identify the most profitable and least profitable items. Next, a textual 
report is generated, including the top 3 products with the highest profit, the bottom 3 products with the lowest profit, 
and a complete ranking of all products based on profitability. If an error occurs, an appropriate error message will be 
returned.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_profitability_report():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        # Calculating numeric and percentage profit for each row
        df["profit"] = df["total_sale"] - df["total_purchase"]
        df["profit_percent"] = np.where(
            df["total_purchase"] > 0,
            np.round((df["profit"] / df["total_purchase"]) * 100, 2),
            0
        )

        # Grouping by product
        grouped = df.groupby("product_name").agg({
            "profit": "sum",
            "total_purchase": "sum",
            "total_sale": "sum"
        })

        # Calculating profitability percentage for each product
        grouped["profit_percent"] = np.where(
            grouped["total_purchase"] > 0,
            np.round((grouped["profit"] / grouped["total_purchase"]) * 100, 2),
            0
        )

        # Sorting by total profit
        sorted_by_profit = grouped.sort_values(by="profit", ascending=False)

        # Displaying products with highest profit and loss
        most_profitable = sorted_by_profit.head(3)
        most_loss = sorted_by_profit.tail(3)

        report_lines = []

        report_lines.append("💰 Top profitable products: ")
        for name, row in most_profitable.iterrows():
            report_lines.append(
                f"  • {name}: Profit {row['profit']:,.0f} Dollars ({row['profit_percent']}%)"
            )

        report_lines.append("\n Least profitable products (Loss):")
        for name, row in most_loss.iterrows():
            report_lines.append(
                f"  • {name}: Profit {row['profit']:,.0f} Dollars ({row['profit_percent']}%)"
            )

        report_lines.append("\n📊 Complete product ranking based on profit:")
        for name, row in sorted_by_profit.iterrows():
            report_lines.append(
                f"  • {name}: Profit {row['profit']:,.0f} Dollars ({row['profit_percent']}%)"
            )

        return "\n".join(report_lines)

    except Exception as e:
        return f"⚠️ Error generating profitability report: {e}"
