# report2.py
"""
Diese Funktion ruft Daten aus der Datenbank „sales.db“ ab und berechnet den Gesamtgewinn sowie den Rentabilitätsprozentsatz 
für jedes Produkt. Zunächst werden der numerische Gewinn und der prozentuale Gewinn für jede Zeile berechnet. Anschließend 
werden die Daten nach Produktname gruppiert, um den gesamten Einkaufsbetrag, den gesamten Verkaufsbetrag, den Gesamtgewinn 
und den Gewinnprozentsatz für jedes Produkt zu ermitteln. Die Produkte werden nach Gesamtgewinn sortiert, um die 
profitabelsten und am wenigsten profitablen Artikel zu identifizieren. Danach wird ein Textbericht erstellt, der die drei 
Produkte mit dem höchsten Gewinn, die drei Produkte mit dem niedrigsten Gewinn sowie eine vollständige Rangliste aller 
Produkte basierend auf ihrer Rentabilität enthält. Falls während der Ausführung ein Fehler auftritt, wird eine entsprechende 
Fehlermeldung zurückgegeben.

"""


import sqlite3
import pandas as pd
import numpy as np

def generate_profitability_report():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        # Berechnung des numerischen und prozentualen Gewinns für jede Zeile
        df["profit"] = df["total_sale"] - df["total_purchase"]
        df["profit_percent"] = np.where(
            df["total_purchase"] > 0,
            np.round((df["profit"] / df["total_purchase"]) * 100, 2),
            0
        )

        # Nach Produkt gruppieren
        grouped = df.groupby("product_name").agg({
            "profit": "sum",
            "total_purchase": "sum",
            "total_sale": "sum"
        })

        # Berechnung des Rentabilitätsprozentsatzes für jedes Produkt
        grouped["profit_percent"] = np.where(
            grouped["total_purchase"] > 0,
            np.round((grouped["profit"] / grouped["total_purchase"]) * 100, 2),
            0
        )

        # Sortierung nach Gesamtgewinn
        sorted_by_profit = grouped.sort_values(by="profit", ascending=False)

        # Anzeige der Produkte mit dem höchsten Gewinn und Verlust
        most_profitable = sorted_by_profit.head(3)
        most_loss = sorted_by_profit.tail(3)

        report_lines = []

        report_lines.append("💰 Top rentable Produkte: ")
        for name, row in most_profitable.iterrows():
            report_lines.append(
                f"  • {name}: Gewinn {row['profit']:,.0f} Euro ({row['profit_percent']}%)"
            )

        report_lines.append("\n Am wenigsten rentable Produkte (Verlust):")
        for name, row in most_loss.iterrows():
            report_lines.append(
                f"  • {name}: Gewinn {row['profit']:,.0f} Euro ({row['profit_percent']}%)"
            )

        report_lines.append("\n📊 Vollständige Produktbewertung basierend auf Gewinn:")
        for name, row in sorted_by_profit.iterrows():
            report_lines.append(
                f"  • {name}: Gewinn {row['profit']:,.0f} Euro ({row['profit_percent']}%)"
            )

        return "\n".join(report_lines)

    except Exception as e:
        return f"⚠️ Fehler beim Erstellen des Rentabilitätsberichts: {e}"
