# report4.py
"""
This function reads product sales and purchase data from the sales.db database and provides a comprehensive analysis of 
inventory status. For each product, profit amount and sales percentage relative to purchase quantity are calculated.  
Then, the data is grouped by product to derive the average purchase price, highest sales price, total profit, and sales 
percentage. High-selling, low-selling, high-profit, and low-profit products are identified. A textual report is generated,
including sales percentages, pricing impact, and classification of weak and strong products in terms of sales and profitability.  
If an error occurs, an appropriate message will be returned.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_inventory_analysis():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        # Calculating profit and sales percentage relative to inventory
        df["profit"] = df["total_sale"] - df["total_purchase"]
        df["sold_percent"] = np.where(
            df["quantity_purchased"] > 0,
            np.round((df["quantity_sold"] / df["quantity_purchased"]) * 100, 2),
            0
        )

        # Grouping by product
        grouped = df.groupby("product_name").agg({
            "quantity_purchased": "sum",
            "quantity_sold": "sum",
            "purchase_price": "mean",
            "selling_price": "max",
            "profit": "sum",
            "sold_percent": "mean"
        })

        # Identifying the least-selling products
        low_sales = grouped.sort_values(by="quantity_sold").head(3)

        # Identifying the best-selling products
        top_sales = grouped.sort_values(by="quantity_sold", ascending=False).head(3)

        # Identifying low-profit products
        low_profit = grouped.sort_values(by="profit").head(3)

        # High-profit products
        top_profit = grouped.sort_values(by="profit", ascending=False).head(3)

        lines = []

        lines.append("🛒 Sales percentage relative to inventory:")
        for name, row in grouped.iterrows():
            lines.append(f"  • {name}: {row['sold_percent']}٪ Already Sold")

        lines.append("\n💸 Pricing Impact:")
        for name, row in grouped.iterrows():
            lines.append(f"  • {name}: Purchase {row['purchase_price']:.0f} / Maximum Sales {row['selling_price']:.0f}")

        lines.append("\n📉 Low-Selling and Low-Profit Products:")
        for name in set(low_sales.index).union(low_profit.index):
            row = grouped.loc[name]
            lines.append(f"  • {name}: Sale {row['quantity_sold']} / Profit {row['profit']:,.0f} Dollars")

        lines.append("\n📈 High-Selling and High-Profit Products:")
        for name in set(top_sales.index).union(top_profit.index):
            row = grouped.loc[name]
            lines.append(f"  • {name}: Sale {row['quantity_sold']} / Profit {row['profit']:,.0f} Dollars")

        return "\n".join(lines)

    except Exception as e:
        return f"⚠️ Inventory Analysis Error: {e}"
