#Seven Gunthrope Elbow assignment

#imports (i forgot the pyplot for some reason and was stuck for like 15 minutes until i realized)
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pandas import DataFrame
#Here is the data after a certain point i just started writing thousands because i didn't want duplicates
data = {
    #X COLUMN
    'x':
#Spent 5 minutes on a same length error to find out i hit the period key and made two values a decimal all good now
[12,34,22,15,2,67,43,23,44,89,123,63,267,345,43,56,61,
345,231,76,47,11,96,20,341,678,64,22,90,34,54,89,31,890,80,10,
55,27,51,500,501,478,198,848,456,276,1000,111,311,777,1243,11175,54556,0,13121],
    #Y COLUMN
    'y':
# Wanted to use random seed but didn't understand it enough
[1,4,6,222,333,213,312,444,44,90,555,616,535,353,754,39,49,59,19,7,8,9,67,98,
97,56,5654,8788,2341,896,996,978,3333,1111,95,1123,7837,8271,
6276,9000,9128,1983,1783,6712,1090,2025,1500,8383,5411,
1177,9090,23542,43143,0,12111]
}
df=DataFrame(data,columns=['x','y'])
distances = []
#ELBOW after 30 minutes i realized i put for k in k which was just overwriting the variable.... i got it though
kl = range(1,10)
# Good old for loop
for k in kl :
    Clusterinfo = kmeanmodel = KMeans(n_clusters=k).fit(df)
    distances.append(Clusterinfo.inertia_)
## Plot plotting the graph it looks good identified the elbow it seems to be at 6 on the x-axis adding and taking out values never really moved it
plt.plot(kl,distances, 'bo-')
plt.xlabel('K-Clusters')
plt.ylabel('Distance')
plt.title('Cluster Values and Distances')
plt.show()