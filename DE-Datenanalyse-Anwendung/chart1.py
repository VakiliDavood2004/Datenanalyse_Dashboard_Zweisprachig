# chart.py
"""
Dieser Code verwendet pandas und matplotlib, um die Rentabilität von Produkten aus der sales.db-Datenbank zu analysieren.
Zunächst werden die Einkaufs- und Verkaufsdaten der Produkte gelesen und der Gewinn für jeden Artikel berechnet.
Anschließend wird ein Balkendiagramm erstellt, um die Rentabilität darzustellen:
Produkte mit positivem Gewinn werden in Grün angezeigt, solche mit negativem Gewinn in Rot.
In der ersten Funktion wird das Diagramm in einem separaten Fenster angezeigt.
In der zweiten Funktion wird das Diagramm als Pixmap-Bild für die grafische Benutzeroberfläche gerendert.

"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📉 Darstellung des Diagramms in einem unabhängigen Fenster
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
        plt.title("📉 Diagramm zur Rentabilität von Produkten")
        plt.xlabel("Produktname")
        plt.ylabel("Gesamtgewinn (Euro)")
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
        print(f"⚠️ Fehler beim Erstellen des Rentabilitätsdiagramms: {e}")

# 🖼️ Erstellen eines Diagrammbildes für die 
def get_profit_chart_pixmap():
    try:
        conn = sqlite3.connect("sales.db")
        query = "SELECT product_name, total_purchase, total_sale FROM sales"
        df = pd.read_sql_query(query, conn)
        conn.close()

        df["profit"] = df["total_sale"] - df["total_purchase"]
        product_profit = df.groupby("product_name")["profit"].sum().sort_values()
        colors = ["green" if p >= 0 else "red" for p in product_profit]

        fig, ax = plt.subplots(figsize=(8, 4))  # 👈 Kleinere Größe für die Hauptseite
        bars = ax.bar(product_profit.index, product_profit.values, color=colors)
        ax.set_title("📉 Diagramm zur Rentabilität von Produkten", fontsize=12)
        ax.set_xlabel("Produktname")
        ax.set_ylabel("Gesamtgewinn (Euro)")
        ax.set_xticks(range(len(product_profit.index)))
        ax.set_xticklabels(product_profit.index, rotation=45, ha="right")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️ Fehler beim Erstellen des Diagrammbildes {e}")
        return None
