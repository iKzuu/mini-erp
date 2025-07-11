from front_page import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec()