from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class TransactionEditDialog(QDialog):
    def __init__(self, table, row):
        super(TransactionEditDialog, self).__init__()
        uic.loadUi("ui/transactionEditDialog.ui", self)
        
        self.table = table
        self.row = row
        
        