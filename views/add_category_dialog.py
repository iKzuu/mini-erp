from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class AddCategoryDialog(QDialog):
    def __init__(self, parent=None):
        super(AddCategoryDialog, self).__init__(parent)
        uic.loadUi("ui/addCategoryDialog.ui", self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.closeBtn.clicked.connect(self.close)
        self.addBtn.clicked.connect(self.add_category)
        self.cancelBtn.clicked.connect(self.reject)
        
    def add_category(self):
        self.accept()
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()