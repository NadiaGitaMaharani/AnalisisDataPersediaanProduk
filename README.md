# TUGAS PENGKODEAN DAN PEMROGRAMAN KELAS F - NADIA GITA MAHARANI

# DIBUAT OLEH
Nama : Nadia Gita Maharani

NIM : 12030122130100

Kelas : F

# DATA
Pembelian:
Pada tanggal 2024-06-01, PT. XYZ membeli 10 unit Produk A dari Supplier A dengan harga satuan Rp 10.000.
Pada tanggal 2024-06-03, PT. XYZ membeli 5 unit Produk B dari Supplier B dengan harga satuan Rp 15.000.
Pada tanggal 2024-06-05, PT. XYZ membeli 8 unit Produk C dari Supplier C dengan harga satuan Rp 20.000.
Pada tanggal 2024-06-07, PT. XYZ membeli 15 unit Produk D dari Supplier D dengan harga satuan Rp 25.000.

Retur Pembelian:
Pada tanggal 2024-06-05, PT. XYZ mengembalikan 2 unit Produk A karena rusak.
Pada tanggal 2024-06-08, PT. XYZ mengembalikan 1 unit Produk B karena salah kirim.
Pada tanggal 2024-06-09, PT. XYZ mengembalikan 5 unit Produk D karena tidak sesuai pesanan.

Penjualan:
Pada tanggal 2024-06-02, PT. XYZ menjual 3 unit Produk A kepada Customer A dengan harga satuan Rp 12.000.
Pada tanggal 2024-06-04, PT. XYZ menjual 2 unit Produk B kepada Customer B dengan harga satuan Rp 18.000.
Pada tanggal 2024-06-06, PT. XYZ menjual 5 unit Produk C kepada Customer C dengan harga satuan Rp 22.000.
Pada tanggal 2024-06-08, PT. XYZ menjual 4 unit Produk D kepada Customer D dengan harga satuan Rp 27.000.

Retur Penjualan:
Pada tanggal 2024-06-06, Customer A mengembalikan 1 unit Produk A karena tidak sesuai.
Pada tanggal 2024-06-09, Customer C mengembalikan 2 unit Produk C karena kualitas buruk.
Pada tanggal 2024-06-10, Customer D mengembalikan 1 unit Produk D karena salah produk.

Persediaan:
Menghitung stok akhir dari masing-masing produk dengan memperhitungkan semua transaksi di atas.

# LANGKAH ANALISIS DATA
Berikut adalah langkah-langkah analisis data berdasarkan semua kode yang telah diberikan:
1. Pengumpulan Data
   - Tabel Pembelian:
     - Mengumpulkan data tentang jumlah dan jenis produk yang dibeli dari berbagai pemasok beserta tanggal pembelian dan harga satuan.
   - Tabel Retur Pembelian:
     - Mengumpulkan data tentang jumlah dan jenis produk yang dikembalikan ke pemasok beserta tanggal pengembalian dan alasannya.
   - Tabel Penjualan:
     - Mengumpulkan data tentang jumlah dan jenis produk yang dijual kepada pelanggan beserta tanggal penjualan dan harga jual satuan.
   - Tabel Retur Penjualan:
     - Mengumpulkan data tentang jumlah dan jenis produk yang dikembalikan oleh pelanggan beserta tanggal pengembalian dan alasannya.
   - Tabel Persediaan:
     - Mengumpulkan data tentang stok akhir dari setiap produk setelah memperhitungkan semua transaksi di atas.
2. Persiapan Data
   - Menggabungkan data dari tabel-tabel tersebut menjadi satu set data yang terstruktur dan bersih untuk analisis.
   - Menghitung total pembelian, penjualan, retur pembelian, dan retur penjualan untuk setiap produk.
3. Visualisasi Data
   - Bar Plot untuk Transaksi Produk:
     - Menggunakan diagram batang untuk menampilkan jumlah pembelian, retur pembelian, penjualan, dan retur penjualan untuk setiap produk.
   - Bar Plot untuk Stok Akhir:
     - Menggunakan diagram batang untuk menampilkan stok akhir dari setiap produk.
4. Analisis Pergerakan Stok Harian
   - Membuat diagram garis untuk menampilkan perubahan stok harian dari setiap produk.
   - Menganalisis bagaimana stok berubah setiap hari berdasarkan transaksi yang terjadi.

Dengan mengikuti langkah-langkah di atas, Anda dapat melakukan analisis data yang komprehensif menggunakan tabel pembelian, retur pembelian, penjualan, retur penjualan, dan persediaan. Visualisasi data membantu dalam memahami pola dan tren dalam transaksi dan persediaan produk.

### a. PT XYZ memiliki 4 ruang penyimpanan untuk menyimpan produk A, B, C, dan D. Di antara keempat ruangan tersebut, terdapat satu ruangan yang memiliki luas ruangan terbesar. Sehingga Manajer Gudang membutuhkan informasi 'Pergerakan Stok Harian' untuk mempertimbangkan persediaan apa yang akan diletakkan di gudang penyimpanan terluas tersebut.
![Figure_1](https://github.com/NadiaGitaMaharani/PengkodeanDanPemrograman-Python-AnalisisData/assets/167200610/4f81a1d5-31d8-4622-84eb-9ac9bb38dafd)
Interpretasi : Dari linechart tersebut, dapat dilihat bahwa ternyata produk yang membutuhkan penyimpanan terluas adalah Produk D.

### b. PT XYZ memiliki kebijakan untuk selalu menyimpan persediaan minimal 5 unit dalam gudang. Manajer pembeluan membutuhkan informasi "Stok Akhir Produk" untuk mengetahui persediaan produk yang kurang dari 5 unit untuk dilakukan pembelian.
![Figure_2](https://github.com/NadiaGitaMaharani/PengkodeanDanPemrograman-Python-AnalisisData/assets/167200610/2fee648d-bc38-4d69-8d2e-e5bc62be02ce)
Interpretasi : Dari histogram tersebut, dapat dilihat bahwa stok Produk B hanya 2 unit sehingga Manajer Pembelian harus melakukan pembelian.

### c. Produk apa yang perlu dipertimbangkan kembali pemasoknya karena terlalu banyak retur pembelian yang dilakukan?
![Figure_3](https://github.com/NadiaGitaMaharani/PengkodeanDanPemrograman-Python-AnalisisData/assets/167200610/bbd45368-11f7-44a8-9725-bc553507ca6b)
Interpretasi : Dari histogram tersebut, dapat dilihat bahwa retur pembelian terbanyak dilakukan atas Produk A, walaupun jika dilihat frekuensi tertinggi adalah Produk D. Produk A dilakukan retur pembelian 2 unit dari 10 unit yang dibeli (1 dari 2 unit), sedangkan Produk D dilakukan retur pembelian 5 unit dari 15 unit yang dibeli (1 dari 3 unit).
