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
