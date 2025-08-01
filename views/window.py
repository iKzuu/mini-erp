from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QToolButton, QFileDialog, QWidget, QHBoxLayout, QPushButton, QHeaderView
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtChart
import resources_rc
import data_dummy
from .stock_edit_dialog import StockEditDialog
from .supplier_edit_dialog import SupplierEditDialog
from .transaction_edit_dialog import TransactionEditDialog
from .category_edit_dialog import CategoryEditDialog
from .warehouse_edit_dialog import WarehouseEditDialog
from .user_edit_dialog import UserEditDialog
from .history_edit_dialog import HistoryEditDialog
from .delete_data_dialog import DeleteDataDialog

# from modules.inventory.services.scanner_service import ScannerService

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/minierp_cool.ui", self)
        
        # Side menu
        # Hide icon only sidebar when app start
        self.icon_only_widget.hide()
        
        # Connect hamburgerButton clicked
        self.hamburgerBtn1.clicked.connect(self.toggleSidebar)
        self.hamburgerBtn2.clicked.connect(self.toggleSidebar)

        # Switch Page
        
        # Switch to overview
        self.overviewBtn1.clicked.connect(lambda: self.switch_page(0))
        self.overviewBtn2.clicked.connect(lambda: self.switch_page(0))

        # Switch to stock
        self.stockBtn1.clicked.connect(lambda: self.switch_page(1))
        self.stockBtn2.clicked.connect(lambda: self.switch_page(1))

        # Switch to supplier
        self.supplierBtn1.clicked.connect(lambda: self.switch_page(2))
        self.supplierBtn2.clicked.connect(lambda: self.switch_page(2))

        # Swtich to transaction
        self.transactionBtn1.clicked.connect(lambda: self.switch_page(3))
        self.transactionBtn2.clicked.connect(lambda: self.switch_page(3))
        
        # Switch to category
        self.categoryBtn1.clicked.connect(lambda: self.switch_page(4))
        self.categoryBtn2.clicked.connect(lambda: self.switch_page(4))
        
        # Switch to warehouse
        self.warehouseBtn1.clicked.connect(lambda: self.switch_page(5))
        self.warehouseBtn2.clicked.connect(lambda: self.switch_page(5))
        
        # Switch to user
        self.userBtn1.clicked.connect(lambda: self.switch_page(6))
        self.userBtn2.clicked.connect(lambda: self.switch_page(6))
        
        # Swtich to history
        self.historyBtn1.clicked.connect(lambda: self.switch_page(7))
        self.historyBtn2.clicked.connect(lambda: self.switch_page(7))
        
        # Choose file
        self.chooseFileBtn.clicked.connect(self.open_file)
        
        prev_btn = self.calendarWidget.findChild(QToolButton, "qt_calendar_prevmonth")
        next_btn = self.calendarWidget.findChild(QToolButton, "qt_calendar_nextmonth")
        
        prev_btn.setText("<")
        next_btn.setText(">")
        
        # load data dummy
        self.load_data()

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)
    
    # Choose file function
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Pilih File",
            "",
            "All Files (*);;Text Files (*.txt);;Images (*.png *.jpg)"
        )
        # if file_path:
        #     ScannerService.scan_barang(file_path)

    # Function for load dummy data from data_dummy.py
    def load_data(self):
        
        tables = [
            {
                "table": self.stockTableWidget,
                "headers": ["ID", "Kode Barang", "Nama Barang", "Satuan", "Harga Beli", "Harga Jual", "Stock", "Deskripsi", ""],
                "data": data_dummy.dummy_stock
            },
            {
                "table": self.supplierTableWidget,
                "headers": ["ID", "ID Barang", "Nama", "Telepon", "Alamat", ""],
                "data": data_dummy.dummy_supplier
            },
            {
                "table": self.transactionTableWidget,
                "headers": ["ID", "ID Barang", "ID Gudang", "Tanggal", "Jenis", "Jumlah", "Keterangan", ""],
                "data": data_dummy.dummy_transaction
            },
            {
                "table": self.categoryTableWidget,
                "headers": ["ID", "ID Gudang", "Nama", "Deskripsi", ""],
                "data": data_dummy.dummy_category
            },
            {
                "table": self.warehouseTableWidget,
                "headers": ["ID", "Nama Warehouse", "Keterangan", "Lokasi", ""],
                "data": data_dummy.dummy_warehouse
            },
            {
                "table": self.userTableWidget,
                "headers": ["ID", "Nama Lengkap", "Password", "Role", "Refresh Token", "Sign Status", ""],
                "data": data_dummy.dummy_user
            },
            {
                "table": self.historyTableWidget,
                "headers": ["ID", "ID Pengguna", "ID Entitas", "ID Gudang", "Waktu", "Aksi", "Entitas", "Before Data", "After Data", "Keterangan", ""],
                "data": data_dummy.dummy_history
            }
        ]
        
        for info in tables:
            table = info["table"]
            headers = info["headers"]
            data = info["data"]
            
            row_count = len(data)
            column_count = len(headers)
            
            table.setRowCount(row_count)
            table.setColumnCount(column_count)
            table.setHorizontalHeaderLabels(headers)
            
            self.adjust_table_columns(table, len(headers) - 1)

            for row_num, row_data in enumerate(data):
                for col_num, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    table.setItem(row_num, col_num, item)
                    
                self.add_crud_buttons(table, row_num)
                
    def adjust_table_columns(self, table, action_column_index):
        header = table.horizontalHeader()
        header.setStretchLastSection(False)
        for col in range(table.columnCount()):
            if col == action_column_index:
                header.setSectionResizeMode(col, QHeaderView.ResizeToContents)
            else:
                header.setSectionResizeMode(col, QHeaderView.Stretch)
            
    def add_crud_buttons(self, table, row):
        widget = QWidget()
        widget.setStyleSheet("background: transparent;")
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(30)
        layout.setAlignment(Qt.AlignCenter)

        # Edit Button
        btn_edit = QPushButton()
        btn_edit.setIcon(QIcon(":/icons/edit-blue.svg"))
        btn_edit.setIconSize(QSize(16, 16))
        btn_edit.setStyleSheet(
            """
                QPushButton{
                    border: none;
                    background: transparent;
                    border-radius: 5px;
                    padding:5px;
                }
                QPushButton:hover{
                    background-color: #D9D9D9;
                }
            """)
        
        # Delete Button
        btn_delete = QPushButton()
        btn_delete.setIcon(QIcon(":/icons/delete-blue.svg"))
        btn_delete.setIconSize(QSize(16, 16))
        btn_delete.setStyleSheet(
            """
                QPushButton{
                    border: none;
                    background: transparent;
                    border-radius: 5px;
                    padding:5px;
                }
                QPushButton:hover{
                    background-color: #D9D9D9;
                }
            """)
        
        btn_edit.clicked.connect(lambda _, b=btn_edit: self.edit_row(table, b))
        btn_delete.clicked.connect(lambda _, b=btn_delete: self.delete_row(table, b))

        layout.addWidget(btn_edit)
        layout.addWidget(btn_delete)
        widget.setLayout(layout)

        col_index = table.columnCount() - 1

        # add widget to cell
        table.setCellWidget(row, col_index, widget)

        # Biar cell Action tidak bisa di-select
        dummy_item = QTableWidgetItem()
        dummy_item.setFlags(Qt.NoItemFlags)
        table.setItem(row, col_index, dummy_item)

        # Resize kolom Action agar pas
        header = table.horizontalHeader()
        header.setSectionResizeMode(col_index, QHeaderView.ResizeToContents)
        
    def edit_row(self, table, button):
        index = table.indexAt(button.parent().pos())
        row = index.row()
        table_name = table.objectName()
        
        if table_name == "stockTableWidget":
            dialog = StockEditDialog(table, row)
        elif table_name == "supplierTableWidget":
            dialog = SupplierEditDialog(table, row)
        elif table_name == "transactionTableWidget":
            dialog = TransactionEditDialog(table, row)
        elif table_name == "categoryTableWidget":
            dialog = CategoryEditDialog(table, row)
        elif table_name == "warehouseTableWidget":
            dialog = WarehouseEditDialog(table, row)
        elif table_name == "userTableWidget":
            dialog = UserEditDialog(table, row)
        elif table_name == "historyTableWidget":
            dialog = HistoryEditDialog(table, row)
        else:
            print(f"Table {table} not found")
        
        dialog.exec_()

    def delete_row(self, table, button):
        # find real-time row
        index = table.indexAt(button.parent().pos())
        row = index.row()
        
        dialog = DeleteDataDialog(table, row)
        dialog.exec_()

    def toggleSidebar(self):
        if self.icon_text_widget.isVisible():
            self.icon_text_widget.hide()
            self.icon_only_widget.show()
        else:
            self.icon_text_widget.show()
            self.icon_only_widget.hide()