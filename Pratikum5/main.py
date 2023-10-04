import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc

Data = np.array([[2,4,4,3], [3,4,3,5], [4,3,2,5], [1,5,4,2], [3,2,1,3]])
print(Data)
print("\n")

# plt.figure(figsize=(7, 10))
plt.title('Dendogram')
cluster = shc.linkage(Data, method='single', metric='cityblock')
shc.dendrogram(Z=cluster)
plt.show()
