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
