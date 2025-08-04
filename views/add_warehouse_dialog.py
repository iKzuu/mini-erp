from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class AddWarehouseDialog(QDialog):
    def __init__(self, parent=None):
        super(AddWarehouseDialog, self).__init__(parent)
        uic.loadUi("ui/addWarehouseDialog.ui", self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.closeBtn.clicked.connect(self.close)
        self.cancelBtn.clicked.connect(self.reject)
        self.addBtn.clicked.connect(self.add_warehouse)
        
    def add_warehouse(self):
        self.accept()
        
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
        