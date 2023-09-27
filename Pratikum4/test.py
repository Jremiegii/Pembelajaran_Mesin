from sklearn.cluster import KMeans
import numpy as np

# Data numberik yang akan dilakukan cluster
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto").fit(X)
# Parameter pada code diatas:
# 1. n_clusters     : Jumlah cluster yang ingin dibuat.
# 2. random_state   : Menentukan seed yang digunakan untuk memilih titik pusat cluster secara random.
# 2. n_init         : Jumlah iterasi yang akan dilakukan.
# 4. fit            : Melakukan proses clustering.

# Mendapatkan label cluster dari masing-masing titik data.
print(kmeans.labels_)

# Memprediksi cluster dari dua titik data baru atau nilai cetroid  yaitu [1, 2] dan [10, 2]
# print(kmeans.predict([[0, 0], [12, 3]]))
print(kmeans.predict([[1, 2], [10, 2]]))

# Mendapatkan titik pusat dari masing-masing cluster.
print(kmeans.cluster_centers_)
