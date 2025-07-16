from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
import resources_rc

class StockEditDialog(QDialog):
    def __init__(self, table, row):
        super(StockEditDialog, self).__init__()
        uic.loadUi("ui/stockDialog.ui", self)
        
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
        
        self.closeBtn.clicked.connect(self.close)
        self.cancelBtn.clicked.connect(self.close)
        self.saveBtn.clicked.connect(lambda: self.save_edited_data)
        
    def save_edited_data(self):
        print("Saved")
        
    # Function for dragable dialog window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()