# chart5.py
"""
Dieser Code ruft Verkaufsdaten aus der Datenbank sales.db ab, um die Verkaufstrends verschiedener Produkte im Zeitverlauf zu analysieren.  
Transaktionsdaten werden in das Datetime-Format konvertiert, und die Daten werden nach Datum und Produktname gruppiert, um die täglichen 
Gesamtverkäufe jedes Artikels zu berechnen. Ein Liniendiagramm wird erstellt, um Änderungen im Verkaufsverlauf darzustellen, wobei jedes 
Produkt durch eine eigene Linie repräsentiert wird. Die erste Funktion zeigt das Diagramm in einem separaten Fenster an, während die 
zweite Funktion dasselbe Diagramm als Pixmap-Bild für die grafische Benutzeroberfläche rendert.

"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# ⏳ Erstellung eines Liniendiagramms der Produktverkäufe im Zeitverlauf
def draw_sales_line_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold, transaction_date FROM sales", conn)

        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df_grouped = df.groupby(["transaction_date", "product_name"])["quantity_sold"].sum().unstack().fillna(0)

        plt.figure(figsize=(10, 6))
        for column in df_grouped.columns:
            plt.plot(df_grouped.index, df_grouped[column], label=column)

        plt.title("📈 Verkaufstrend der Produkte im Zeitverlauf")
        plt.xlabel("Datum")
        plt.ylabel("Verkaufte Einheiten")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Fehler beim Zeichnen des Verkaufs-Liniendiagramms: {e}")

