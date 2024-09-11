# chart4.py
"""
Dieser Code verwendet Verkaufsdaten aus der Datenbank sales.db, um den prozentualen Anteil der Verkäufe jedes Produkts im 
Verhältnis zum Gesamtumsatz zu berechnen und stellt die Ergebnisse in einem Kreisdiagramm dar. Jeder Abschnitt des Diagramms 
ist farblich codiert, und sowohl der Verkaufsanteil in Prozent als auch die Anzahl der verkauften Einheiten werden neben 
jedem Segment angezeigt. Die erste Funktion zeigt das Diagramm in einem separaten Fenster an, während die zweite Funktion 
dasselbe Diagramm als Pixmap-Bild zur Anzeige in der grafischen Benutzeroberfläche generiert.

"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap

# 📊 Darstellung des Kreisdiagramms mit dem Verkaufsanteil jedes Produkts
def draw_sold_percentage_pie_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query(
                "SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        total_sold = product_sales.sum()

        if total_sold == 0:
            print("⚠️Es wurden keine Verkäufe aufgezeichnet.")
            return

        labels = product_sales.index
        values = product_sales.values
        colors = plt.cm.Paired.colors[:len(labels)]

        plt.figure(figsize=(8, 6))
        plt.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*total_sold)} Stück)",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        plt.title("Prozentualer Verkaufsanteil jedes Produkts am Gesamtumsatz", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Fehler beim Erstellen des Verkaufs-Kreisdiagramms: {e}")
