import pandas as pd

url = "D:\Coding\Pembelajaran Mesin\Pembelajaran_Mesin\Pratikum2\Data\MoviesTopRated.csv"
df = pd.read_csv(url)
print(df) # Mencetak data pada csv

# print(df.head()) # Menampilkan 5 data teratas

# print(df.head(10)) # Menampilkan 10 data

# print(df.tail()) # Menampilkan 5 data paling akhir

# print(df.tail(10)) # Menampilkan 10 data paling akhir

# print(df.sample(10)) # Menampilkan 10 data secara acak

# print(df.count()) # Menampilkan nama kolom dan jumlah keseluruhan data pada baris

# print(df.shape[0]) # Menampilkan jumlah keseluruhan data pada baris baris

# print(df.shape[1]) # Menampilkan jumlah kolom

# print(df.shape) # Menampilkan dimensi dari dataframe

# print(df.dtypes) # Menampilkan struktur dari data

# print(df.info()) # Menampilkan struktur dari data secara detail

# print(df.describe(include="all")) # Menampilkan informasi statistik pada setiap kolom seperti nilai minimum, nilai maksimum, standar deviasi, rata-rata dan sebagainya

# print(df[['id', 'title', 'release_date']].head()) # Menampilkan isi dari kolom id, title dan release date

# print(df[(df.vote_average >= 7)].head()) # Menampilkan data yang difilter berdasarkan vote average > 7