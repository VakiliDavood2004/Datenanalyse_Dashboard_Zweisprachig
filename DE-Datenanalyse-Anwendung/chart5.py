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

# 🖼️ Generierung eines Verkaufsdiagrammbildes zur Anzeige im Dashboard
def get_sales_line_chart_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold, transaction_date FROM sales", conn)

        df["transaction_date"] = pd.to_datetime(df["transaction_date"])
        df_grouped = df.groupby(["transaction_date", "product_name"])["quantity_sold"].sum().unstack().fillna(0)

        fig, ax = plt.subplots(figsize=(8, 5))
        for column in df_grouped.columns:
            ax.plot(df_grouped.index, df_grouped[column], label=column)

        ax.set_title("📈 Verkaufstrend der Produkte im Zeitverlauf", fontsize=12)
        ax.set_xlabel("Datum")
        ax.set_ylabel("Verkaufte Einheiten")
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.4)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️ Fehler beim Generieren des Verkaufsdiagrammbildes: {e}")
        return None
