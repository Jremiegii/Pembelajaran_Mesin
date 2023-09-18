import pandas as pd
import matplotlib.pyplot as plt

url = "D:\Coding\Pembelajaran Mesin\Pembelajaran_Mesin\Pratikum3\Data\Startups in 2012-2021.csv"
df = pd.read_csv(url)

def transform_valuation(valuasi):
    if valuasi < 10:
        return 0
    elif valuasi < 100:
        return 1
    elif valuasi < 1000:
        return 2
    elif valuasi < 10000:
        return 3
    else:
        return 4

clos = ['Date Joined', 'City', 'Select Investors']
df = df.drop(clos, axis=1)

print(df.info())

print(df.isna().sum()) # Mengecek jumlah data yang hilang

df['Valuation ($B)'] = df['Valuation ($B)'].str.strip("$") # Menghapus tanda $

df['Valuation ($B)'] = df['Valuation ($B)'].apply(float) # Mengubah tipe data object menjadi float
print(df.info())

df['Valuation ($B)'] = df['Valuation ($B)'].apply(transform_valuation) # Melakukan transformasi data

print(df.head())

plt.hist(df['Valuation ($B)']) # Manampilkan histogram

# print(df['Valuation ($B)'].hist())


# # Atur label sumbu x dan y serta judul grafik (opsional)
# plt.xlabel('Nilai')
# plt.ylabel('Frekuensi')
# plt.title('Histogram Nilai')

# Tampilkan grafik
plt.show()
