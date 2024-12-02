# report3.py
"""
This function retrieves sales data from the sales.db database and enables temporal analysis by converting transaction 
dates into datetime format. Rows lacking valid dates are removed first. Then, purchase and sales data are grouped and 
aggregated on a daily and monthly basis. The peak sales day is identified, and reports are generated for monthly sales 
trends and product performance by month. Finally, a textual report is produced, including the highest sales day, monthly 
trends, and product performance for each month. If an error occurs, an appropriate warning message will be returned.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_time_analysis():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        # Convert date column to datetime format
        df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors='coerce')

        # Remove rows with invalid or missing dates
        df = df.dropna(subset=["transaction_date"])

        # Daily and monthly grouping
        daily_summary = df.groupby(df["transaction_date"].dt.date).agg({
            "total_sale": "sum",
            "total_purchase": "sum"
        })

        monthly_summary = df.groupby(df["transaction_date"].dt.to_period("M")).agg({
            "total_sale": "sum",
            "total_purchase": "sum"
        }).sort_index()

        # Best-selling day
        peak_day = daily_summary["total_sale"].idxmax()
        peak_day_value = daily_summary["total_sale"].max()

        # Monthly sales trend
        trend_lines = ["📆 Monthly sales trend:"]
        for period, row in monthly_summary.iterrows():
            trend_lines.append(
                f"  • {period}: Sales {row['total_sale']:,.0f} Purchase / Dollars {row['total_purchase']:,.0f} Dollars"
            )

        # Product sales over time
        product_trend = df.groupby(["product_name", df["transaction_date"].dt.to_period("M")])["quantity_sold"].sum()
        product_lines = ["📦 Monthly product sales trend:"]
        product_trend = product_trend.sort_index()
        for (name, period), qty in product_trend.items():
            product_lines.append(f"  • {name} in {period}: {qty} units")

        # Report Summary
        report = [
            f"⏳ Peak sales day: {peak_day} With amount {peak_day_value:,.0f} Dollars",
            "",
        ] + trend_lines + [""] + product_lines

        return "\n".join(report)

    except Exception as e:
        return f"⚠️ Error in temporal sales analysis: {e}"