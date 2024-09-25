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
