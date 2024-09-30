# report1.py
"""
Diese Funktion erstellt einen zusammenfassenden Bericht basierend auf den Daten, die in der Datenbank "sales.db" 
gespeichert sind. Sie extrahiert Informationen wie die Anzahl der Datensätze, die Anzahl der unterschiedlichen Produkte, 
die gesamten Einkäufe und Verkäufe, den Gesamtgewinn sowie die höchsten und niedrigsten Verkaufszahlen. Anschließend 
berechnet sie für jedes Produkt die gesamte Verkaufsmenge und den Gesamtverkaufswert und liefert einen strukturierten 
Textbericht. Falls während der Ausführung ein Fehler auftritt, wird eine entsprechende Fehlermeldung als Zeichenkette 
zurückgegeben.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_summary():
