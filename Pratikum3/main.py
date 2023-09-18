import pandas as pd

# Membaca file CSV
url = "D:\Coding\Pembelajaran Mesin\Pembelajaran_Mesin\Pratikum3\Data\Train.csv"
df = pd.read_csv(url)
# print(df)

# Menampilkan jumlah kolom dan baris
print(f'Dimensi : {df.shape}') # Dimensi matrix
print(f'Jumlah Baris: {df.shape[0]}') # Jumlah baris
print(f'Jumlah Kolom: {df.shape[1]}') # Jumlah kolom
print("\n")

# Menampilkan 5 data teratas dan terbawah
print("Data 5 teratas: ")
print(df.head()) # 5 data teratas
print("Data 5 terbawah: ")
print(df.tail()) # 5 data terbawah
print("\n")

# Menampilkan data yang hilang
print(df.isna().sum())
print(df.info())
# Jumlah data yang hilang terdapat pada atribut:
# 1. Age sebanyak 177 (891 - 714)
# 2. Cabin sebanyak 687 (891 - 204)
# 3. Embarked sebanyak 2 (891 - 889)
print("\n")

# # Mengahpus atribut yang tidak penting atau tidak bermakna
cols = ['Name', 'Ticket', 'Cabin']
df = df.drop(cols, axis=1)
print(df.info())
print("\n")

# Menghapus data yang hilang(NaNs) atau kosong
df = df.dropna()
print(df.isna().sum())
print(df.info())
print("\n")

# Mengubah variabel kategorikal dalam sebuah DataFrame menjadi variabel dummy atau one-hot encoding.
# Setiap kategori dalam variabel kategorikal akan diubah menjadi sebuah kolom baru dalam DataFrame yang hanya berisi nilai 0 atau 1. 
# Kolom ini akan menunjukkan apakah observasi (baris) tertentu termasuk dalam kategori tersebut (1) atau tidak (0).
# Jika hasil dari operasi one-hot encoding menghasilkan lebih banyak kolom daripada jumlah kategori unik dalam variabel asli.
# Maka, mungkin terjadi karena beberapa alasan: 
# 1. Variabel kategorikal dengan banyak kategori unik
# 2. Kategori kosong atau hilang
# 3. Perbedaan dalam data training dan data pengujian
dummies = []
cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
    dummies.append(pd.get_dummies(df[col]))

titanic_dummies = pd.concat(dummies, axis=1)
df = pd.concat([df, titanic_dummies], axis=1)
df = df.drop(['Pclass', 'Sex', 'Embarked'], axis=1)
print(df.info())
print("\n")

# Mengisi data yang hilang
print(df.isna().sum())
df['Age'] = df['Age'].interpolate() # Mengisi data berdasarkan nilai interpolasi
# df['Age'] = df['Age'].median() # Mengisi data berdasarkan nilai median
print(df.isna().sum())
print(df.info())
