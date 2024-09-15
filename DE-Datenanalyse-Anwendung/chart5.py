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
