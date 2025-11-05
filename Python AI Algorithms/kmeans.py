#Seven Gunthrope K-Means(normal) assignment

#imports the right way this time! pyplot!
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pandas import DataFrame
#The DATA
data = {
    #X COLUMN
    'x':
#Spent 1 minute on the same decimal i precopied the values before i removed the decimals to this file...
[12,34,22,15,2,67,43,23,44,89,123,63,267,345,43,56,61,
345,231,76,47,11,96,20,341,678,64,22,90,34,54,89,31,890,80,10,
55,27,51,500,501,478,198,848,456,276,1000,111,311,777,1243,11175,54556,0],
    #Y COLUMN
    'y':
[1,4,6,222,333,213,312,444,44,90,555,616,535,353,754,39,49,59,19,7,8,9,67,98,
97,56,5654,8788,2341,896,996,978,3333,1111,95,1123,7837,8271,
6276,9000,9128,1983,1783,6712,1090,2025,1500,8383,5411,
1177,9090,23542,43143,0]
}
df=DataFrame(data,columns=['x','y'])
#Clusters/K-means normal not ++ i think it's 6 clusters but 5 is possible since it was barely moving but 6 did not at all
kmeans = KMeans(n_clusters=6).fit(df)
centroids = kmeans.cluster_centers_
# No more for loop
## Plotting the scatter forgot a comma pycharm saved me, also scatter looks a bit weird but is accurate
# most values are on the smaller side while having outliers being the 11000s and up
plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float))
plt.scatter(centroids[:,0], centroids[:,1], c='red')
plt.show()