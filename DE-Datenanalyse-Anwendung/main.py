import sys
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QHBoxLayout, QLabel, QTableWidget, QScrollArea, QDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Project files
from report1 import generate_summary
from report2 import generate_profitability_report
from report3 import generate_time_analysis
from report4 import generate_inventory_analysis

from chart1 import draw_profit_bar_chart, get_profit_chart_pixmap
from chart2 import draw_profit_pie_chart, get_profit_pie_pixmap
from chart3 import draw_inventory_bar_chart, get_inventory_chart_pixmap
from chart4 import draw_sold_percentage_pie_chart, get_sold_percentage_pie_pixmap
from chart5 import draw_sales_line_chart, get_sales_line_chart_pixmap
from chart6 import draw_sales_bar_chart, get_sales_bar_chart_pixmap
from chart7 import draw_sales_share_pie_chart, get_sales_share_pie_pixmap

from read_me import show_readme
from file import create_database, load_csv_and_insert, display_existing_data


def show_scrollable_dialog(parent, title, content):
    dialog = QDialog(parent)
    dialog.setWindowTitle(title)
    dialog.resize(600, 500)
    layout = QVBoxLayout(dialog)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    label = QLabel(content)
    label.setWordWrap(True)

    scroll_content = QWidget()
    content_layout = QVBoxLayout(scroll_content)
    content_layout.addWidget(label)

    scroll.setWidget(scroll_content)
    layout.addWidget(scroll)
    dialog.exec_()
