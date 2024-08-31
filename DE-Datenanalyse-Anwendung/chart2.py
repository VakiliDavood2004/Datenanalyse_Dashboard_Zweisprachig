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
