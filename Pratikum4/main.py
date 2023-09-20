import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Visualisasi
import seaborn as sns
import matplotlib.pyplot as pyplot
sns.set(style="darkgrid")

# Membaca file CSV
url = "D:\Coding\Pembelajaran Mesin\Pembelajaran_Mesin\Pratikum4\Data\iris.csv"
df_iris = pd.read_csv(url)

sns.pairplot(df_iris)

x = df_iris.iloc[:, [0,1,2,3]].values
#Finding the optimum number of clusters for k-means classification
from sklearn.cluster import KMeans
WCSS = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    WCSS.append(kmeans.inertia_)
#Plotting the results onto a line graph, allowing us to observe 'The elbow'
plt.plot(range(1, 11), WCSS)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()

#Applying kmeans to the dataset / Creating the kmeans classifier
kmeans = KMeans (n_clusters = i, init = 'k-means++', max_iter =  300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)

#visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Iris-sentosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Iris-virginica')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroid')
plt.legend()
plt.show()