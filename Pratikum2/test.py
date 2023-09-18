import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Memuat data Movie ke dalam dataframe pandas
movie = pd.read_csv('D:\Coding\Pembelajaran Mesin\Pembelajaran_Mesin\Pratikum2\Data\MoviesTopRated.csv')
print("\n============================================")
print("\tRichardo Teddy_215314015")
print("\tFransiskus Jremiegi S_205314062")
print("============================================")
# Menghitung beberapa statistik dasar menggunakan numpy
mean_vote = np.mean(movie['vote_average'])
median_vote = np.median(movie['vote_count'])
max_vote = np.max(movie['vote_average'])
min_vote = np.min(movie['vote_average'])
std_vote = np.std(movie['vote_average'])

# Menampilkan deskripsi statistik untuk semua kolom
print("============================================")
print("\tDaftar Data Movie")
print("============================================")
print(movie)

# Mencetak hasil

print("Skor Minimum Vote              : ", min_vote)
print("Skor Median  Vote              : ", median_vote)
print("Skor Maksimum Vote             : ", max_vote)
print("Rata-rata Vote  : ", mean_vote)
print("Standar deviasi Vote : ", std_vote)

# Membuat histogram jumlah Vote Movie 
plt.hist(movie['vote_average'], bins=6, color='red')
plt.title('Distribution Rated of the Movie')
plt.xlabel('Vote Rated')
plt.ylabel('Jumlah')
plt.show()

#Memfilter data rate movie diatas 7
print("============================================")
print("\tRated Movie diatas 7")
print("============================================")
movie[(movie.vote_average >= 7.0)].head()