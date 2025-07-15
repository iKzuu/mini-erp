# Stock Table
dummy_stock = [
    [1, "BRG001", "Pensil", "Alat tulis", "PCS", 1000, 1500, 50],
    [2, "BRG002", "Buku Tulis", "Buku 40 lembar", "PCS", 3000, 5000, 100],
    [3, "BRG003", "Penghapus", "Penghapus karet", "PCS", 500, 800, 75],
    [4, "BRG004", "Pulpen", "Pulpen tinta hitam", "PCS", 2000, 3500, 40],
]

# Supplier Table
dummy_supplier = [
    [1, "BRG001", "PT. Alat Tulis Jaya", "021-555111", "Jl. Merdeka No.10"],
    [2, "BRG002", "CV. Buku Murah", "021-555222", "Jl. Sudirman No.20"],
    [3, "BRG003", "Toko Penghapus Abadi", "021-555333", "Jl. Mangga Dua No.30"],
]

# Transaction Table
dummy_transaction = [
    [1, "BRG001", "GDG001", "2024-09-25", "IN", 100, "Pembelian barang"],
    [2, "BRG002", "GDG001", "2024-09-26", "OUT", 50, "Penjualan barang"],
    [3, "BRG003", "GDG002", "2024-09-27", "IN", 200, "Retur pembelian"],
]

# Category Table
dummy_category = [
    [1, "GDG001", "ATK", "Kategori alat tulis kantor"],
    [2, "GDG001", "Buku", "Kategori buku sekolah"],
]

# Warehouse Table
dummy_warehouse = [
    [1, "Gudang Utama", "Pusat distribusi barang", "Jakarta"],
    [2, "Gudang Cabang", "Stok barang cadangan", "Surabaya"],
]

# User Table
dummy_user = [
    [1, "Admin Utama", "hashed_password_1", "Admin", "refresh_token_1", "Active"],
    [2, "Staff Gudang", "hashed_password_2", "Staff", "refresh_token_2", "Inactive"],
]

# History Table
dummy_history = [
    [1, "USR001", "BRG001", "GDG001", "2024-09-25 10:00:00", "UPDATE", "Barang", "Stok: 50", "Stok: 100", "Penyesuaian Stok"],
    [2, "USR002", "SUP001", "GDG001", "2024-09-26 11:30:00", "INSERT", "Supplier", "-", "PT. Supplier Baru", "Tambah Supplier"],
]