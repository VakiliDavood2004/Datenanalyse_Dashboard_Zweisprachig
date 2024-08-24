from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def show_readme(parent=None):
    text = """
        💻 Projektübersicht
    """

    dialog = QDialog(parent)
    dialog.setWindowTitle("📘 User Guide")
    dialog.resize(800, 600)

