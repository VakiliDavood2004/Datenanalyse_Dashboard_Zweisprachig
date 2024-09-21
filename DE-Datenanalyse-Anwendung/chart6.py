# chart6.py
"""
Dieser Code extrahiert Verkaufsdaten aus der Datenbank sales.db und berechnet die Gesamtanzahl der verkauften Einheiten 
für jedes Produkt. Anschließend wird ein Balkendiagramm erstellt, das die Produkte nach Verkaufsmenge – von am wenigsten 
bis am meisten verkauft – sortiert darstellt. Die Balken sind in der Farbe „mediumseagreen“ eingefärbt.Die erste Funktion 
zeigt das Diagramm zur visuellen Prüfung in einem separaten Fenster an, während die zweite Funktion dasselbe Diagramm als 
Pixmap-Bild für die grafische Benutzeroberfläche oder das Dashboard generiert. Über jedem Balken wird die Verkaufsanzahl 
als Zahlenwert angezeigt.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap
# 📦 Erstellung eines Balkendiagramms der meist- und am wenigsten verkauften Produkte
def draw_sales_bar_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query("SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum().sort_values()

        plt.figure(figsize=(10, 6))
        bars = plt.bar(product_sales.index, product_sales.values, color="mediumseagreen")
        plt.title("📦 Produktverkäufe (von niedrig bis hoch)", fontsize=14)
        plt.xlabel("Produktname")
        plt.ylabel("Verkaufte Einheiten")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.3)

        for bar, value in zip(bars, product_sales.values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     str(int(value)), ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Fehler beim Zeichnen des Produktverkaufsdiagramms: {e}")
