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
