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

    layout = QVBoxLayout(dialog)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    label = QLabel(text)
    label.setWordWrap(True)
    
    # Schriftart-Einstellungen für QLabel
    font = QFont("Iranian Sans", 10)  # Sie können die Schriftart ändern.
    label.setFont(font)
    
    # Rand- und Innenabstand-Einstellungen
    label.setStyleSheet("padding: 10px;")

    scroll.setWidget(label)
    layout.addWidget(scroll)

    dialog.exec_()