# chart2.py
"""
Dieser Code verwendet Daten aus der sales.db-Datenbank, um den Gewinn von Produkten zu berechnen, die positive Erträge erzielt haben.
Anschließend wird ein Kreisdiagramm erstellt, das den relativen Anteil des Gewinns jedes Produkts darstellt.
Grüne Segmente kennzeichnen profitable Produkte, und auf jedem Abschnitt des Diagramms werden Prozentangaben angezeigt.
Die erste Funktion zeigt das Diagramm in einem separaten Fenster an, während die zweite Funktion dasselbe Diagramm als Pixmap-Bild 
für die grafische Benutzeroberfläche generiert.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📊 Anzeige des Kreisdiagramms zum Produktgewinn in einem separaten 
def draw_profit_pie_chart():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT product_name, total_purchase, total_sale FROM sales", conn)
        conn.close()

        df["profit"] = df["total_sale"] - df["total_purchase"]
        product_profit = df.groupby("product_name")["profit"].sum()
        positive = product_profit[product_profit > 0]

        if positive.empty:
            print("⚠️ Es gibt keine profitablen Produkte zur Anzeige im Diagramm.")
            return

        labels = positive.index
        values = positive.values
        colors = ["green"] * len(positive)

        plt.figure(figsize=(8, 6))
        plt.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*sum(values)):,} €)",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        plt.title("Relativer Gewinnanteil der Produkte", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Fehler beim Erstellen des Gewinn-Kreisdiagramms: {e}")

# 🖼️ Erstellung eines Diagrammbildes zur Anzeige auf der Hauptseite
def get_profit_pie_pixmap():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT product_name, total_purchase, total_sale FROM sales", conn)
        conn.close()

        df["profit"] = df["total_sale"] - df["total_purchase"]
        product_profit = df.groupby("product_name")["profit"].sum()
        positive = product_profit[product_profit > 0]

        if positive.empty:
            return None

        labels = positive.index
        values = positive.values
        colors = ["green"] * len(positive)

        fig, ax = plt.subplots(figsize=(6.5, 5))
        ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        ax.set_title("Relativer Gewinnanteil der Produkte", fontsize=12)

        buffer = BytesIO()
        fig.tight_layout()
        fig.savefig(buffer, format="png")
        buffer.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.getvalue())
        plt.close(fig)
        return pixmap

    except Exception as e:
        print(f"⚠️ Fehler beim Generieren des Gewinn-Kreisdiagrammbildes: {e}")
        return None
