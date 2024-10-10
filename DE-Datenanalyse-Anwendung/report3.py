# report3.py
"""
Diese Funktion ruft Verkaufsdaten aus der Datenbank sales.db ab und ermöglicht eine zeitliche Analyse, indem 
Transaktionsdaten in das Datumsformat konvertiert werden. Zeilen ohne gültiges Datum werden zunächst entfernt. 
Anschließend werden Einkaufs- und Verkaufsdaten täglich und monatlich gruppiert und aggregiert. Der umsatzstärkste 
Tag wird ermittelt, und es werden Berichte zu monatlichen Verkaufstrends sowie zur Produktleistung pro Monat erstellt. 
Abschließend wird ein Textbericht generiert, der den umsatzstärksten Tag, die monatlichen Trends und die Produktleistung 
für jeden Monat enthält. Im Falle eines Fehlers wird eine entsprechende Warnmeldung zurückgegeben.

"""


import sqlite3
import pandas as pd
import numpy as np

