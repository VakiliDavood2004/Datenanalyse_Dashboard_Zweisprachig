# report1.py
"""
Diese Funktion erstellt einen zusammenfassenden Bericht basierend auf den Daten, die in der Datenbank "sales.db" 
gespeichert sind. Sie extrahiert Informationen wie die Anzahl der Datensätze, die Anzahl der unterschiedlichen Produkte, 
die gesamten Einkäufe und Verkäufe, den Gesamtgewinn sowie die höchsten und niedrigsten Verkaufszahlen. Anschließend 
berechnet sie für jedes Produkt die gesamte Verkaufsmenge und den Gesamtverkaufswert und liefert einen strukturierten 
Textbericht. Falls während der Ausführung ein Fehler auftritt, wird eine entsprechende Fehlermeldung als Zeichenkette 
zurückgegeben.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_summary():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        row_count = len(df)
        total_purchase = df["total_purchase"].sum()
        total_sale = df["total_sale"].sum()
        profit = total_sale - total_purchase
        unique_products = df["product_code"].nunique()
        max_sale_qty = df["quantity_sold"].max()
        min_sale_qty = df["quantity_sold"].min()

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        product_values = df.groupby("product_name")["total_sale"].sum()

        report_lines = [
            f"📊 Allgemeiner Lagerbericht: ",
            f"- Anzahl der Einträge: {row_count}",
            f"- Anzahl unterschiedlicher Artikel: {unique_products}",
            f"- Gesamter Einkaufsbetrag: {total_purchase:,.0f} Euro",
            f"- Gesamter Verkaufsbetrag: {total_sale:,.0f} Euro",
            f"- Gesamtgewinn {profit:,.0f} Euro",
            f"- Höchstes Verkaufsvolumen: {max_sale_qty}",
            f"- Niedrigstes Verkaufsvolumen: {min_sale_qty}",
            "",
            f"🔹 Verkäufe nach Produkt:"
        ]

        for product in product_sales.index:
            qty = product_sales[product]
            value = product_values[product]
            report_lines.append(f"  • {product}: {qty} Menge, Gesamtverkaufsbetrag: {value:,.0f} Euro")

        return "\n".join(report_lines)

    except Exception as e:
        return f"⚠️ Fehler beim Generieren des Berichts: {e}"
