# file.py
"""
This code implements a simple system for managing product sales data. First, the create_database function creates a 
database with a custom name and sets up a sales table with a suitable structure for storing purchase and sales information. 
Then, the CSV file uploaded by the user is processed, its columns are rewritten to match the database format, 
and total purchase and sales columns are calculated. The processed data is added to the database and displayed 
in a graphical table within the user interface. Previously stored data in the database can also be displayed in 
the same table. If an error occurs at any stage, an appropriate message is shown to the user.

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
            'Transaction Date': 'transaction_date'  # The date is entered by the user
        }, inplace=True)

        data['total_purchase'] = data['purchase_price'] * data['quantity_purchased']
        data['total_sale'] = data['selling_price'] * data['quantity_sold']

        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
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
        print(f"Error inserting into the database: {e}")
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
        parent_widget, "Select CSV file", "", "CSV Files (*.csv);;All Files (*)"
    )

    if file_name:
        data = load_and_process_csv(file_name)
        if data is not None:
            display_data(data, table_widget)
            success = import_csv_to_db(file_name, db_name)
            if success:
                QMessageBox.information(parent_widget, "Success", "CSV file has been successfully inserted into the database.")
            else:
                QMessageBox.critical(parent_widget, "Error", "Failed to insert data into the database.")
        else:
            QMessageBox.critical(parent_widget, "Error", "CSV file processing failed.")

def display_existing_data(db_name, table_widget):
    try:
        conn = sqlite3.connect(db_name)
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        table_widget.setRowCo   unt(len(df))
        table_widget.setColumnCount(len(df.columns))
        table_widget.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                table_widget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))
    except Exception as e:
        print(f"Error loading previous data: {e}")
