# report4.py
"""
Diese Funktion liest Verkaufs- und Einkaufsdaten von Produkten aus der Datenbank sales.db und liefert eine umfassende 
Analyse des Lagerbestands. Für jedes Produkt werden der Gewinnbetrag und der Verkaufsprozentsatz im Verhältnis zur 
Einkaufsmenge berechnet. Anschließend werden die Daten nach Produkt gruppiert, um den durchschnittlichen Einkaufspreis, 
den höchsten Verkaufspreis, den Gesamtgewinn und den Verkaufsprozentsatz zu ermitteln. Produkte mit hohen und niedrigen 
Verkaufszahlen sowie mit hohem und niedrigem Gewinn werden identifiziert. Es wird ein Textbericht erstellt, der 
Verkaufsprozentsätze, Preiswirkungen und eine Klassifizierung der schwachen und starken Produkte in Bezug auf Verkauf 
und Rentabilität enthält. Im Falle eines Fehlers wird eine entsprechende Meldung zurückgegeben.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_inventory_analysis():
