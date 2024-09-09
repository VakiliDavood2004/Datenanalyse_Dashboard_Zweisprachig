# chart3.py
"""
Dieser Code liest Daten aus der sales.db-Datenbank, um den verbleibenden Lagerbestand jedes Produkts zu berechnen 
(indem die Anzahl der Verkäufe von der Anzahl der Einkäufe subtrahiert wird) und erstellt anschließend ein Balkendiagramm, 
das die Lagerbestände der Produkte darstellt.Die erste Funktion zeigt das Diagramm in einem separaten Fenster an, sodass 
Benutzer die verbleibende Menge jedes Artikels visuell überprüfen können. Die zweite Funktion rendert dasselbe Diagramm als 
Pixmap-Bild zur Verwendung in der grafischen Benutzeroberfläche. Alle Balken werden in der Farbe Dodgerblue gezeichnet,
wobei numerische Beschriftungen über jedem Balken angezeigt werden.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📉 Darstellung des Lagerbestandsdiagramms in einem separaten Fenster
def draw_inventory_bar_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_purchased, quantity_sold FROM sales", conn)

        df["inventory"] = df["quantity_purchased"] - df["quantity_sold"]
        product_inventory = df.groupby("product_name")["inventory"].sum().sort_values()

        plt.figure(figsize=(10, 5))
        bars = plt.bar(product_inventory.index, product_inventory.values, color="dodgerblue")
        plt.title("📦 Verbleibender Lagerbestand jedes Produkts")
        plt.xlabel("Produktname")
        plt.ylabel("Verbleibende Lageranzahl")
        plt.xticks(rotation=45, ha="right")
        plt.grid(axis="y", linestyle="--", alpha=0.4)

        for bar, value in zip(bars, product_inventory.values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                     str(int(value)), ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Fehler beim Erstellen des Lagerbestandsdiagramms: {e}")

# 🖼️ Umwandlung des Lagerbestandsdiagramms in ein Bild zur Anzeige im Dashboard
def get_inventory_chart_pixmap():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_purchased, quantity_sold FROM sales", conn)
        df["inventory"] = df["quantity_purchased"] - df["quantity_sold"]
        product_inventory = df.groupby("product_name")["inventory"].sum().sort_values()

        fig, ax = plt.subplots(figsize=(8, 4.5))
        bars = ax.bar(product_inventory.index, product_inventory.values, color="dodgerblue")
        ax.set_title("📦 Verbleibender Lagerbestand jedes Produkts", fontsize=12)
        ax.set_xlabel("Produktname")
        ax.set_ylabel("Verbleibende Lageranzahl")
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
        print(f"⚠️ Fehler beim Erzeugen des Lagerbestandsdiagrammbildes: {e}")
        return None
