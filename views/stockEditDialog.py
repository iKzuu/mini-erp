from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class StockEditDialog(QDialog):
    def __init__(self, table, row):
        super(StockEditDialog, self).__init__()
        uic.loadUi("ui/stockDialog.ui", self)
        
        self.table = table
        self.row = row
        
        kode_barang = table.item(row, 1).text()
        nama_barang = table.item(row, 2).text()
        satuan = table.item(row, 3).text()
        harga_beli = table.item(row, 4).text()
        harga_jual = table.item(row, 5).text()
        stock = table.item(row, 6).text()
        deskripsi = table.item(row, 7).text()
        
        self.editKodeBrg.setText(kode_barang)
        self.editNamaBrg.setText(nama_barang)
        self.editSatuan.setText(satuan)
        self.editHargaBli.setText(harga_beli)
        self.editHargaJual.setText(harga_jual)
        self.editStock.setText(stock)
        self.editDeskripsi.setText(deskripsi)
        
        # Make window frameless from default window frame
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.saveBtn.clicked.connect(self.save_edited_data)
        self.cancelBtn.clicked.connect(self.reject)
        
        self.closeBtn.clicked.connect(self.close)
        
    def save_edited_data(self):
        # take data from input
        kode_barang = self.editKodeBrg.text()
        nama_barang = self.editNamaBrg.text()
        satuan = self.editSatuan.text()
        harga_beli = self.editHargaBli.text()
        harga_jual = self.editHargaJual.text()
        stock = self.editStock.text()
        deskripsi = self.editDeskripsi.text()
        
        # update the table data
        self.table.setItem(self.row, 1, self.__new__item(kode_barang))
        self.table.setItem(self.row, 2, self.__new__item(nama_barang))
        self.table.setItem(self.row, 3, self.__new__item(satuan))
        self.table.setItem(self.row, 4, self.__new__item(harga_beli))
        self.table.setItem(self.row, 5, self.__new__item(harga_jual))
        self.table.setItem(self.row, 6, self.__new__item(stock))
        self.table.setItem(self.row, 7, self.__new__item(deskripsi))
        
        self.accept() # to close dialog
     
    # to always create a new QTableWidgetItem
    def __new__item(self, value):
        from PyQt5.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(str(value))
                
    # Function for dragable dialog window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()