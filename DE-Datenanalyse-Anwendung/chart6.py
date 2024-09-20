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
