# chart7.py
"""

Dieser Code extrahiert die Verkaufsanzahl für jedes Produkt aus der Datenbank sales.db und zeigt den Anteil jedes Produkts 
am Gesamtverkauf in einem Kreisdiagramm an. Wenn keine Verkäufe erfasst wurden, wird eine Warnmeldung ausgegeben.Im Diagramm 
wird jedes Produkt mit einer eigenen Farbe dargestellt. Sowohl der prozentuale Anteil als auch die absolute Verkaufszahl 
werden angezeigt.Die erste Funktion zeigt das Diagramm in einem separaten Fenster an, während die zweite Funktion dasselbe 
Diagramm als Pixmap-Bild für die grafische Benutzeroberfläche generiert.

"""


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PyQt5.QtGui import QPixmap
# 🎯 Erstellung eines Kreisdiagramms der Verkaufsanteile der einzelnen Produkte
def draw_sales_share_pie_chart():
    try:
        with sqlite3.connect("sales.db") as conn:
            df = pd.read_sql_query("SELECT product_name, quantity_sold FROM sales", conn)

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        total_sold = product_sales.sum()

        if total_sold == 0:
            print("⚠️ Es wurden keine Verkäufe erfasst.")
            return

        labels = product_sales.index
        values = product_sales.values
        colors = plt.cm.tab20.colors[:len(labels)]

        plt.figure(figsize=(8, 6))
        plt.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*total_sold)} Einheiten)",
            startangle=140,
            wedgeprops={'edgecolor': 'white'}
        )
        plt.title("🥧 Anteil am Gesamtverkauf pro Produkt", fontsize=14)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️Fehler bei der Generierung des Diagramms zur Verkaufsverteilung: {e}")
