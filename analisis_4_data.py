import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV
sales_df = pd.read_csv('sales.csv')
customers_df = pd.read_csv('customers.csv')
products_df = pd.read_csv('products.csv')
regions_df = pd.read_csv('regions.csv')

# Menghapus spasi di sekitar nama kolom
sales_df.columns = sales_df.columns.str.strip()
customers_df.columns = customers_df.columns.str.strip()
products_df.columns = products_df.columns.str.strip()
regions_df.columns = regions_df.columns.str.strip()

# Memeriksa data yang hilang
print("Jumlah nilai yang hilang per kolom (Sales):\n", sales_df.isnull().sum())
print("Jumlah nilai yang hilang per kolom (Customers):\n", customers_df.isnull().sum())
print("Jumlah nilai yang hilang per kolom (Products):\n", products_df.isnull().sum())
print("Jumlah nilai yang hilang per kolom (Regions):\n", regions_df.isnull().sum())

# Memeriksa data yang duplikat
print("Jumlah baris yang duplikat (Sales):", sales_df.duplicated().sum())
print("Jumlah baris yang duplikat (Customers):", customers_df.duplicated().sum())
print("Jumlah baris yang duplikat (Products):", products_df.duplicated().sum())
print("Jumlah baris yang duplikat (Regions):", regions_df.duplicated().sum())

# Memeriksa tipe data
print("Tipe data setiap kolom (Sales):\n", sales_df.dtypes)
print("Tipe data setiap kolom (Customers):\n", customers_df.dtypes)
print("Tipe data setiap kolom (Products):\n", products_df.dtypes)
print("Tipe data setiap kolom (Regions):\n", regions_df.dtypes)

# Mengubah format tanggal di sales_df
sales_df['Tanggal'] = pd.to_datetime(sales_df['Tanggal'])

# Mengkategorikan jenis kelamin di customers_df
customers_df['Jenis_Kelamin'] = customers_df['Jenis_Kelamin'].map({'M': 'Laki-laki', 'F': 'Perempuan'})

# Merge data
merged_df = sales_df.merge(customers_df, on='Pelanggan_ID').merge(products_df, on='Produk_ID').merge(regions_df, on='Pelanggan_ID')

# Memeriksa data setelah transformasi
print("Data setelah transformasi:\n", merged_df.head())

# Membuat subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Distribusi jenis kelamin
sns.countplot(ax=axes[0, 0], x='Jenis_Kelamin', data=merged_df)
axes[0, 0].set_title('Distribusi Jenis Kelamin Pembeli')

# Plot 2: Distribusi jenis barang
sns.countplot(ax=axes[0, 1], x='Nama_y', data=merged_df)
axes[0, 1].set_title('Distribusi Jenis Barang yang Dibeli')

# Plot 3: Jumlah penjualan per hari
merged_df.groupby('Tanggal')['Jumlah'].sum().plot(kind='line', ax=axes[1, 0])
axes[1, 0].set_title('Jumlah Penjualan per Hari')
axes[1, 0].set_xlabel('Tanggal')
axes[1, 0].set_ylabel('Jumlah Penjualan')

# Plot 4: Penjualan per wilayah
sns.countplot(ax=axes[1, 1], x='Wilayah', data=merged_df)
axes[1, 1].set_title('Distribusi Penjualan per Wilayah')

# Menyesuaikan layout
plt.tight_layout()
plt.show()
