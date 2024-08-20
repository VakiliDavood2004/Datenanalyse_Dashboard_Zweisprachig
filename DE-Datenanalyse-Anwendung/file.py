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
