from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def show_readme(parent=None):
    text = """
    💻 **Project Overview**

    This project includes several Python files, a database, CSV files, and a stylesheet, all designed for data analysis, 
    report generation, and visualization through charts.
    
    📂 File Structure:

    📊 7 CHART.PY files for generating various types of charts
    📄 4 REPORT.PY files for generating different types of reports
    ❌ 1 FAIL.PY file for handling file loading
    🖥️ 1 main file MAIN.PY for executing the entire application
    📖 1 README.PY file containing documentation
    📦 1 database file SALES.DB
    🎨 1 stylesheet STYLE.CSS to enhance UI design
    📊 1 data file DATA_SET.CSV
    📄 1 standard format file FORMAT.CSV used for data validation
    
    🧠 Program Functionality

    Each module contains full documentation and internal explanations. To run the application properly, start with the MAIN.PY file.
    
    🧩 User Interface

    After launching the program:
    14 buttons are displayed on the left side of the interface.
    The exact function of each button is shown on the right side.
    The first button is for loading a file, allowing users to input their desired dataset.
    ⚠️ Note: The input data file must strictly follow the format defined in the FORMAT.CSV file to be processed correctly.
    
    🗂️ Data Display

    Once the data is loaded:
    Depending on the size of the file, it may take a moment to fully read the data.
    The dataset will be shown in the first display box of the program.

    📄 Reports and 📊 Charts

    The program contains 4 report boxes, each offering detailed insights based on the dataset.
    It also includes 7 chart boxes, showcasing various visualizations like pie charts, bar charts, line graphs, and more.
    By clicking on a specific report or chart, it will open in a separate, focused view.
    
    With appreciation and best wishes, Davood Vakili
    
    Contact Information
    🌐 Website: https://vakilidavood2004.ir
    📧 Email: vakilidavood2004@gmail.com
    📱 Telegram – WhatsApp – Phone: +98 912 005 9751
    📱 Telegram – WhatsApp – Phone: +98 935 723 6110
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
    
    # Font Settings for QLabel 
    font = QFont("Iranian Sans", 10)  # You can change the font type
    label.setFont(font)
    
    # Margin and Padding Settings
    label.setStyleSheet("padding: 10px;")

    scroll.setWidget(label)
    layout.addWidget(scroll)

    dialog.exec_()