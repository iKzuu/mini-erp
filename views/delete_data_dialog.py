from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class DeleteDataDialog(QDialog):
    def __init__(self, table, row):
        super(DeleteDataDialog, self).__init__()
        uic.loadUi("ui/deleteDialog.ui", self)
        
        self.table = table
        self.row = row
        
        # Make window frameless from default window frame
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.confirmDeleteBtn.clicked.connect(self.confirm_delete)
        self.cancelBtn.clicked.connect(self.reject)
        
        self.closeBtn.clicked.connect(self.close)
    
    # Function for delete data when the confirmDeleteBtn clicked
    def confirm_delete(self):
        self.table.removeRow(self.row)
        self.accept()
    
    # Function for dragable dialog window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()