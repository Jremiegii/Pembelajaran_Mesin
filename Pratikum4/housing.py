import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Baca data
url = "D:\Coding\Pembelajaran Mesin\Pembelajaran_Mesin\Pratikum4\Data\housing.csv"
home_data = pd.read_csv(url, usecols=['longitude', 'latitude', 'median_house_value']) # Hanya menyisakan kolom longitude, latitude dan median_house_value

print(home_data.info())

# Visualisasi data
sns.scatterplot(data = home_data, x = 'longitude', y='latitude', hue='median_house_value')
plt.title('Visualisasi Data')
plt.show()

# Normalisasi data
X_train, X_test, y_train, y_test = train_test_split(home_data[['latitude', 'longitude']], home_data[['median_house_value']], test_size=0.33, random_state=0)

X_train_norm = preprocessing.normalize(X_train)
X_test_norm = preprocessing.normalize(X_test)

# Model
kmeans = KMeans(n_clusters = 3, random_state = 0, n_init='auto')
kmeans.fit(X_train_norm)

sns.scatterplot(data = X_train, x = 'longitude', y = 'latitude', hue = kmeans.labels_)
plt.show()

sns.boxplot(x = kmeans.labels_, y = y_train['median_house_value'])
plt.show()

silhouette_score(X_train_norm, kmeans.labels_, metric='euclidean')

# Memilih nilai k terbaik dari cluster
K = range(2, 8)
fits = []
score = []

for k in K:
    model = KMeans(n_clusters = k, random_state= 0, n_init='auto').fit(X_train_norm)

    # Menambahkan model ke fits
    fits.append(model)

    # Menambahakan silhouette_score ke score
    score.append(silhouette_score(X_train_norm, model.labels_, metric='euclidean'))

# Nilai dari K 2
sns.scatterplot(data = X_train, x = 'longitude', y = 'latitude', hue = fits[0].labels_)
plt.title('K = 2')
plt.show()

# Nilai dari K = 4
sns.scatterplot(data = X_train, x = 'longitude', y = 'latitude', hue = fits[2].labels_)
plt.title('K = 4')
plt.show()

# Nilai dari K = 7
sns.scatterplot(data = X_train, x = 'longitude', y = 'latitude', hue = fits[2].labels_)
plt.title('K = 7')
plt.show()

# Nilai line plot dari K
sns.lineplot(x = K, y = score)
plt.title('Nilai line plot dari K')
plt.show()

# Nilai dari K = 5
sns.scatterplot(data = X_train, x = 'longitude', y = 'latitude', hue = fits[3].labels_)
plt.title('K = 5')
plt.show()

# sns.boxplot(x = fits[3].labels_, y = y_train['median_house_value'])
sns.boxplot(x = fits[3].labels_, y = y_train['median_house_value'])
plt.title('K = 5')
plt.show()


'''

Sumber referensi:
https://www.datacamp.com/tutorial/k-means-clustering-python

'''
