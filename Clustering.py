# Data for K-means clustering
german_data_cluster = german_data[['age', 'amount', 'duration']]
print("Original variables:\n{}" .format(german_data_cluster.head()))
      
german_data_cluster_tr = np.log(german_data_cluster);
print("Log transformed variables:\n{}" .format(german_data_cluster_tr.head()))

#Distribution of transformed variable
fig, ax = plt.subplots(1,3,figsize=(20,5))
plt.suptitle('DISTRIBUTION PLOTS OF TRANSFORMED VARIABLES')
sns.distplot(german_data_cluster_tr['amount'], bins=40, ax=ax[0], axlabel="Credit Amount");
sns.distplot(german_data_cluster_tr['duration'], bins=40, ax=ax[1], color='salmon', axlabel="Duration");
sns.distplot(german_data_cluster_tr['age'], bins=40, ax=ax[2], color='darkviolet', axlabel="Age");

#Finding optimal number of clusters
scaler = StandardScaler()
german_data_cluster_scaled = scaler.fit_transform(german_data_cluster_tr)

#Using the elbow method to define the optimal number of clusters
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(german_data_cluster_scaled)
    distortions.append(kmeanModel.inertia_)
    
#Plotting the elbow method 

plt.figure(figsize=(10,5))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')

# k-means algorithm
k = 4
kmeans = KMeans(n_clusters=k, random_state=0).fit(german_data_cluster_scaled)
german_data['Cluster'] = kmeans.labels_

#Adding the clusters back to the data
german_data['Cluster'] = german_data['Cluster'].astype('category')

#3D scatter plot of the cluster

fig4 = px.scatter_3d(german_data, x='age', y='duration', z='amount',color='Cluster')
fig4.update_layout(height=500, width=700, title_text="3D Map of Cluster")
fig4.show()

#Cluster sizes

cluster_size = german_data.groupby('Cluster', as_index=True).size()
cluster_size

#More insights on cluster behavior

#Countplots to identify segments of customers

sns.set_style('white') 
fig, ax = plt.subplots(3,2,figsize=(21,20))
plt.suptitle('COUNT PLOTS',fontsize=15)
sns.countplot(german_data['job'], ax=ax[0][0], palette=sns.color_palette('RdBu'))
sns.countplot(german_data['housing'], ax=ax[0][1], palette=sns.color_palette('RdBu'))
sns.countplot(german_data['saving_acct'], ax=ax[1][0], palette=sns.color_palette('BuGn_r'))
sns.countplot(german_data['chk_acct'], ax=ax[1][1],palette=sns.color_palette('BuGn_r')[4:])
sns.countplot(german_data['purpose'], ax=ax[2][0], palette=sns.color_palette('RdBu_r'))
sns.countplot(german_data['sex'], ax=ax[2][1],palette=sns.color_palette('RdBu_r'))

ax[2][0].tick_params(labelrotation=45)
ax[0][0].set(xlabel="Job", ylabel="Count")
ax[0][1].set(xlabel="Housing", ylabel="Count")
ax[1][0].set(xlabel="Saving Accounts", ylabel="Count")
ax[1][1].set(xlabel="Checking Accounts", ylabel="Count")
ax[2][0].set(xlabel="Purpose", ylabel="Count")
ax[2][1].set(xlabel="Sex and Status", ylabel="Count")


#Distribution of age in each cluster

cluster0 = german_data[german_data['Cluster']==0]
cluster1 = german_data[german_data['Cluster']==1]
cluster2 = german_data[german_data['Cluster']==2]
cluster3 = german_data[german_data['Cluster']==3]

fig, ax = plt.subplots(4,1,figsize=(10,6), constrained_layout=True, sharex=True)
ax[0].title.set_text('Cluster 0')
ax[1].title.set_text('Cluster 1')
ax[2].title.set_text('Cluster 2')
ax[3].title.set_text('Cluster 3')
ax[0].axes.xaxis.set_visible(False)
ax[1].axes.xaxis.set_visible(False)
ax[2].axes.xaxis.set_visible(False)
sns.distplot(cluster0['age'], color='darkcyan', bins=10, ax=ax[0])
sns.distplot(cluster1['age'], color='steelblue', bins=10, ax=ax[1])
sns.distplot(cluster2['age'], color='sandybrown', bins=10, ax=ax[2])
sns.distplot(cluster3['age'], color='indianred', bins=10, ax=ax[3])
plt.xlabel('Age', fontsize=20)


#Distribution of credit amounts in each cluster 

fig, ax = plt.subplots(4,1,figsize=(10,6), constrained_layout=True, sharex=True)
ax[0].title.set_text('Cluster 0')
ax[1].title.set_text('Cluster 1')
ax[2].title.set_text('Cluster 2')
ax[3].title.set_text('Cluster 3')
ax[0].axes.xaxis.set_visible(False)
ax[1].axes.xaxis.set_visible(False)
ax[2].axes.xaxis.set_visible(False)

sns.distplot(cluster0['amount'], color='darkcyan', bins=10, ax=ax[0])
sns.distplot(cluster1['amount'], color='steelblue', bins=10, ax=ax[1])
sns.distplot(cluster2['amount'], color='sandybrown', bins=10, ax=ax[2])
sns.distplot(cluster3['amount'], color='indianred', bins=10, ax=ax[3])
plt.xlabel('Credit Amount', fontsize=20)


#Distribution of duration in each cluster

fig, ax = plt.subplots(4,1,figsize=(10,6), constrained_layout=True, sharex=True)
ax[0].title.set_text('Cluster 0')
ax[1].title.set_text('Cluster 1')
ax[2].title.set_text('Cluster 2')
ax[3].title.set_text('Cluster 3')
ax[0].axes.xaxis.set_visible(False)
ax[1].axes.xaxis.set_visible(False)
ax[2].axes.xaxis.set_visible(False)

sns.distplot(cluster0['duration'], color='darkcyan', bins=10, ax=ax[0])
sns.distplot(cluster1['duration'], color='steelblue', bins=10, ax=ax[1])
sns.distplot(cluster2['duration'], color='sandybrown', bins=10, ax=ax[2])
sns.distplot(cluster3['duration'], color='indianred', bins=10, ax=ax[3])
plt.xlabel('Duration', fontsize=20)

