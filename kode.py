import matplotlib.pyplot as plt

# Data
tanggal = ["2024-06-01", "2024-06-02", "2024-06-03", "2024-06-04", "2024-06-05", "2024-06-06", "2024-06-07", "2024-06-08", "2024-06-09", "2024-06-10"]
stok_produk_a = [10, 7, 7, 7, 5, 6, 6, 6, 6, 6]  # Example stock movements for Produk A
stok_produk_b = [0, 0, 5, 3, 3, 3, 3, 2, 2, 2]  # Example stock movements for Produk B
stok_produk_c = [0, 0, 0, 0, 8, 3, 3, 3, 5, 5]  # Example stock movements for Produk C
stok_produk_d = [0, 0, 0, 0, 0, 0, 15, 11, 11, 10]  # Example stock movements for Produk D

# Plot
plt.figure(figsize=(12, 6))
plt.plot(tanggal, stok_produk_a, marker='o', label='Produk A')
plt.plot(tanggal, stok_produk_b, marker='o', label='Produk B')
plt.plot(tanggal, stok_produk_c, marker='o', label='Produk C')
plt.plot(tanggal, stok_produk_d, marker='o', label='Produk D')

plt.xlabel('Tanggal')
plt.ylabel('Stok')
plt.title('Pergerakan Stok Harian')
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Data
produk = ["Produk A", "Produk B", "Produk C", "Produk D"]
pembelian = [10, 5, 8, 15]
retur_pembelian = [2, 1, 0, 5]
penjualan = [3, 2, 5, 4]
retur_penjualan = [1, 0, 2, 1]
stok_akhir = [6, 2, 5, 7]

# Bar plot for transactions
fig, ax = plt.subplots(figsize=(12, 6))

bar_width = 0.2
index = range(len(produk))

bar1 = plt.bar(index, pembelian, bar_width, label='Pembelian')
bar2 = plt.bar([i + bar_width for i in index], retur_pembelian, bar_width, label='Retur Pembelian')
bar3 = plt.bar([i + 2 * bar_width for i in index], penjualan, bar_width, label='Penjualan')
bar4 = plt.bar([i + 3 * bar_width for i in index], retur_penjualan, bar_width, label='Retur Penjualan')

plt.xlabel('Produk')
plt.ylabel('Jumlah')
plt.title('Transaksi Produk')
plt.xticks([i + 1.5 * bar_width for i in index], produk)
plt.legend()

# Bar plot for stock
fig, ax = plt.subplots(figsize=(12, 6))

bar = plt.bar(produk, stok_akhir, color='skyblue')

plt.xlabel('Produk')
plt.ylabel('Stok Akhir')
plt.title('Stok Akhir Produk')

# Display plots
plt.tight_layout()
plt.show()
