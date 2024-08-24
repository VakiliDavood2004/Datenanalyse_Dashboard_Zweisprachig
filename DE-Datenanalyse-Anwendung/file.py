# file.py
"""
Dieser Code implementiert ein einfaches System zur Verwaltung von Produktverkaufsdaten.Zunächst erstellt die Funktion 
`create_database` eine Datenbank mit einem benutzerdefinierten Namen und richtet eine Verkaufstabelle mit einer geeigneten 
Struktur zur Speicherung von Einkaufs- und Verkaufsinformationen ein.Anschließend wird die vom Benutzer hochgeladene 
CSV-Datei verarbeitet: Die Spalten werden so umgeschrieben, dass sie dem Format der Datenbank entsprechen, und die 
Gesamtspalten für Einkauf und Verkauf werden berechnet.Die verarbeiteten Daten werden der Datenbank hinzugefügt und in 
einer grafischen Tabelle innerhalb der Benutzeroberfläche angezeigt.Bereits gespeicherte Daten in der Datenbank können 
ebenfalls in derselben Tabelle dargestellt werden.Falls in einem Schritt ein Fehler auftritt, wird eine entsprechende 
Meldung an den Benutzer ausgegeben.

"""


import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            product_code TEXT,
            purchase_price REAL,
            selling_price REAL,
            quantity_purchased INTEGER,
            quantity_sold INTEGER,
            total_purchase REAL,
            total_sale REAL,
            transaction_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_and_process_csv(file_name):
    try:
        data = pd.read_csv(file_name)

        data.rename(columns={
            'Product Name': 'product_name',
            'Product Code': 'product_code',
            'Purchase Price': 'purchase_price',
            'Selling Price': 'selling_price',
            'Quantity Purchased': 'quantity_purchased',
            'Quantity Sold': 'quantity_sold',
            'Transaction Date': 'transaction_date'  # Das Datum wird vom Benutzer eingegeben.
        }, inplace=True)

        data['total_purchase'] = data['purchase_price'] * data['quantity_purchased']
        data['total_sale'] = data['selling_price'] * data['quantity_sold']

        return data
    except Exception as e:
        print(f"Fehler beim Laden der CSV-Datei: {e}")
        return None

def import_csv_to_db(csv_file, db_name):
    try:
        data = load_and_process_csv(csv_file)
        if data is None:
            return False

        conn = sqlite3.connect(db_name)
        data.to_sql('sales', conn, if_exists='append', index=False)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Fehler beim Einfügen in die Datenbank: {e}")
        return False

def display_data(data, table_widget):
    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(len(data.columns))
    table_widget.setHorizontalHeaderLabels(data.columns)
    for i in range(len(data)):
        for j in range(len(data.columns)):
            table_widget.setItem(i, j, QTableWidgetItem(str(data.iat[i, j])))

def load_csv_and_insert(parent_widget, db_name, table_widget):
    file_name, _ = QFileDialog.getOpenFileName(
        parent_widget, "CSV-Datei auswählen", "", "CSV-Datei (*.csv);;Alle Datei (*)"
    )

    if file_name:
        data = load_and_process_csv(file_name)
        if data is not None:
            display_data(data, table_widget)
            success = import_csv_to_db(file_name, db_name)
            if success:
                QMessageBox.information(parent_widget, "Erfolg", "Die CSV-Datei wurde erfolgreich in die Datenbank eingefügt.")
            else:
                QMessageBox.critical(parent_widget, "Fehler", "Daten konnten nicht in die Datenbank eingefügt werden.")
        else:
            QMessageBox.critical(parent_widget, "Fehler", "Verarbeitung der CSV-Datei fehlgeschlagen.")

def display_existing_data(db_name, table_widget):
    try:
        conn = sqlite3.connect(db_name)
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        table_widget.setRowCount(len(df))
        table_widget.setColumnCount(len(df.columns))
        table_widget.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                table_widget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
    except Exception as e:
        print(f"Fehler beim Laden der vorherigen Daten: {e}")
