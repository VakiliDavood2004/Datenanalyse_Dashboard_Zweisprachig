from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def show_readme(parent=None):
    text = """
        💻 Projektübersicht

        Dieses Projekt umfasst mehrere Python-Dateien, eine Datenbank, CSV-Dateien und ein Stylesheet – alle entwickelt 
        für Datenanalyse, Berichterstellung und Visualisierung durch Diagramme.

        📂 Dateistruktur:

        📊 7 CHART.PY-Dateien zur Erstellung verschiedener Diagrammtypen 
        📄 4 REPORT.PY-Dateien zur Erstellung unterschiedlicher Berichte 
        ❌ 1 FAIL.PY-Datei zur Fehlerbehandlung beim Laden von Dateien 
        🖥️ 1 Hauptdatei MAIN.PY zur Ausführung der gesamten Anwendung 
        📖 1 README.PY-Datei mit Dokumentation 
        📦 1 Datenbankdatei SALES.DB 
        🎨 1 Stylesheet STYLE.CSS zur Verbesserung des UI-Designs 
        📊 1 Datendatei DATA_SET.CSV 
        📄 1 Standardformatdatei FORMAT.CSV zur Datenvalidierung

        🧠 Programmfunktionalität

        Jedes Modul enthält eine vollständige Dokumentation und interne Erläuterungen. Zum korrekten Start der Anwendung 
        beginne mit der Datei MAIN.PY.

        🧩 Benutzeroberfläche

        Nach dem Start des Programms: 14 Schaltflächen werden auf der linken Seite der Oberfläche angezeigt.
        ie genaue Funktion jeder Schaltfläche wird rechts dargestellt. Die erste Schaltfläche dient zum Laden einer Datei, 
        über die Benutzer den gewünschten Datensatz eingeben können. 
        
        ⚠️ Hinweis: Die Eingabedatei muss strikt dem Format der Datei FORMAT.CSV entsprechen, damit sie korrekt verarbeitet 
        werden kann.

        🗂️ Datenanzeige

        Nach dem Laden der Daten: Je nach Dateigröße kann es einen Moment dauern, bis alle Daten gelesen wurden. Der 
        Datensatz wird im ersten Anzeigefeld des Programms dargestellt.

        📄 Berichte und 📊 Diagramme

        Das Programm enthält 4 Berichtsfelder, die jeweils detaillierte Einblicke basierend auf dem Datensatz bieten. 
        Es gibt zudem 7 Diagrammfelder mit verschiedenen Visualisierungen wie Kreisdiagrammen, Balkendiagrammen, 
        Liniendiagrammen und mehr. Durch Anklicken eines bestimmten Berichts oder Diagramms wird dieser in einer 
        separaten Ansicht geöffnet.

        Mit Dank und den besten Wünschen, Davood Vakili
        
        Kontaktinformationen
        🌐 Webseite: https://vakilidavood2004.ir 
        📧 E-Mail: vakilidavood2004@gmail.com 
        📱 Telegram – WhatsApp – Telefon: +98 912 005 9751 
        📱 Telegram – WhatsApp – Telefon: +98 935 723 6110 
        🔗 LinkedIn: https://www.linkedin.com/in/davood-vakili/ 
        💻 GitHub: https://github.com/VakiliDavood2004/        

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