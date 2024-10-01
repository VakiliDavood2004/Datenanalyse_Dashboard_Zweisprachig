    try:
        conn = sqlite3.connect("sales.db")
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()

        row_count = len(df)
        total_purchase = df["total_purchase"].sum()
        total_sale = df["total_sale"].sum()
        profit = total_sale - total_purchase
        unique_products = df["product_code"].nunique()
        max_sale_qty = df["quantity_sold"].max()
        min_sale_qty = df["quantity_sold"].min()

        product_sales = df.groupby("product_name")["quantity_sold"].sum()
        product_values = df.groupby("product_name")["total_sale"].sum()

        report_lines = [
            f"📊 Allgemeiner Lagerbericht: ",
            f"- Anzahl der Einträge: {row_count}",
            f"- Anzahl unterschiedlicher Artikel: {unique_products}",
            f"- Gesamter Einkaufsbetrag: {total_purchase:,.0f} Euro",
            f"- Gesamter Verkaufsbetrag: {total_sale:,.0f} Euro",
            f"- Gesamtgewinn {profit:,.0f} Euro",
            f"- Höchstes Verkaufsvolumen: {max_sale_qty}",
            f"- Niedrigstes Verkaufsvolumen: {min_sale_qty}",
            "",
            f"🔹 Verkäufe nach Produkt:"
        ]
