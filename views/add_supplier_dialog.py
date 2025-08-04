from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class AddSupplierDialog(QDialog):
    def __init__(self, parent=None):
        super(AddSupplierDialog, self).__init__(parent)
        uic.loadUi("ui/addSupplierDialog.ui", self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.closeBtn.clicked.connect(self.close)
        self.addBtn.clicked.connect(self.add_supplier)
        self.cancelBtn.clicked.connect(self.reject)
        
    def add_supplier(self):
        
        # logic here
        
        self.accept()
        
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()