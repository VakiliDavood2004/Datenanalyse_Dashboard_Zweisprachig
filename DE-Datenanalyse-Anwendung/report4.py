# report4.py
"""
Diese Funktion liest Verkaufs- und Einkaufsdaten von Produkten aus der Datenbank sales.db und liefert eine umfassende 
Analyse des Lagerbestands. Für jedes Produkt werden der Gewinnbetrag und der Verkaufsprozentsatz im Verhältnis zur 
Einkaufsmenge berechnet. Anschließend werden die Daten nach Produkt gruppiert, um den durchschnittlichen Einkaufspreis, 
den höchsten Verkaufspreis, den Gesamtgewinn und den Verkaufsprozentsatz zu ermitteln. Produkte mit hohen und niedrigen 
Verkaufszahlen sowie mit hohem und niedrigem Gewinn werden identifiziert. Es wird ein Textbericht erstellt, der 
Verkaufsprozentsätze, Preiswirkungen und eine Klassifizierung der schwachen und starken Produkte in Bezug auf Verkauf 
und Rentabilität enthält. Im Falle eines Fehlers wird eine entsprechende Meldung zurückgegeben.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_inventory_analysis():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        # Berechnung von Gewinn und Verkaufsprozentsatz im Verhältnis zum Lagerbestand
        df["profit"] = df["total_sale"] - df["total_purchase"]
        df["sold_percent"] = np.where(
            df["quantity_purchased"] > 0,
            np.round((df["quantity_sold"] / df["quantity_purchased"]) * 100, 2),
            0
        )

        # Gruppierung nach Produkt
        grouped = df.groupby("product_name").agg({
            "quantity_purchased": "sum",
            "quantity_sold": "sum",
            "purchase_price": "mean",
            "selling_price": "max",
            "profit": "sum",
            "sold_percent": "mean"
        })

        # Identifizierung der am wenigsten verkauften Produkte
        low_sales = grouped.sort_values(by="quantity_sold").head(3)

        # Identifizierung der meistverkauften Produkte
        top_sales = grouped.sort_values(by="quantity_sold", ascending=False).head(3)

        # Identifizierung von Produkten mit geringem Gewinn
        low_profit = grouped.sort_values(by="profit").head(3)

        # Produkte mit hohem Gewinn
        top_profit = grouped.sort_values(by="profit", ascending=False).head(3)

        lines = []

        lines.append("🛒 Verkaufsprozentsatz im Verhältnis zum Lagerbestand:")
        for name, row in grouped.iterrows():
            lines.append(f"  • {name}: {row['sold_percent']}٪ Bereits verkauft")

        lines.append("\n💸 Pricing Impact:")
        for name, row in grouped.iterrows():
            lines.append(f"  • {name}: Einkauf {row['purchase_price']:.0f} / Maximaler Verkauf {row['selling_price']:.0f}")

        lines.append("\n📉 Produkte mit geringem Verkauf und geringem Gewinn:")
        for name in set(low_sales.index).union(low_profit.index):
            row = grouped.loc[name]
            lines.append(f"  • {name}: Verkauf {row['quantity_sold']} / Gewinn {row['profit']:,.0f} Euro")

        lines.append("\n📈 Produkte mit hohem Verkauf und hohem Gewinn:")
        for name in set(top_sales.index).union(top_profit.index):
            row = grouped.loc[name]
            lines.append(f"  • {name}: Verkauf {row['quantity_sold']} / Gewinn {row['profit']:,.0f} Euro")

        return "\n".join(lines)

    except Exception as e:
        return f"⚠️ Fehler bei der Lagerbestandsanalyse: {e}"
