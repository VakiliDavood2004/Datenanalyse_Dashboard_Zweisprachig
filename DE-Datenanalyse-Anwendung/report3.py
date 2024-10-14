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

def generate_time_analysis():
    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        # Datumsspalte in das Datumsformat konvertieren
        df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors='coerce')

        # Zeilen mit ungültigen oder fehlenden Datumsangaben entfernen
        df = df.dropna(subset=["transaction_date"])

        # Tägliche und monatliche Gruppierung
        daily_summary = df.groupby(df["transaction_date"].dt.date).agg({
            "total_sale": "sum",
            "total_purchase": "sum"
        })

        monthly_summary = df.groupby(df["transaction_date"].dt.to_period("M")).agg({
            "total_sale": "sum",
            "total_purchase": "sum"
        }).sort_index()

        # Umsatzstärkster Tag
        peak_day = daily_summary["total_sale"].idxmax()
        peak_day_value = daily_summary["total_sale"].max()

        # Monatlicher Verkaufstrend
        trend_lines = ["📆 Monatlicher Verkaufstrend:"]
        for period, row in monthly_summary.iterrows():
            trend_lines.append(
                f"  • {period}: Verkäufe {row['total_sale']:,.0f} Einkauf / Euro {row['total_purchase']:,.0f} Euro"
            )

        # Produktverkäufe im Zeitverlauf
        product_trend = df.groupby(["product_name", df["transaction_date"].dt.to_period("M")])["quantity_sold"].sum()
        product_lines = ["📦 Monatlicher Verkaufs­trend nach Produkt:"]
        product_trend = product_trend.sort_index()
        for (name, period), qty in product_trend.items():
            product_lines.append(f"  • {name} in {period}: {qty} Einheiten")

        # Berichtszusammenfassung
        report = [
            f"⏳ Spitzenverkaufstag: {peak_day} Mit Betrag {peak_day_value:,.0f} Euro",
            "",
        ] + trend_lines + [""] + product_lines

        return "\n".join(report)

    except Exception as e:
        return f"⚠️ Fehler bei der zeitlichen Verkaufsanalyse: {e}"