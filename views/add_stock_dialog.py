from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class AddStockDialog(QDialog):
    def __init__(self, parent=None):
        super(AddStockDialog, self).__init__(parent)
        uic.loadUi("ui/addStockDialog.ui", self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.closeBtn.clicked.connect(self.close)
        self.addBtn.clicked.connect(self.add_stock)
        self.cancelBtn.clicked.connect(self.reject)
        
    def add_stock(self):
        self.accept()
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
        