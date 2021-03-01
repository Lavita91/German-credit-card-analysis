    
  #Project summary plots 
  plot('n_credits')
  plot('job')
  plot('present_emp')
  plot('sex')
  plot('credit_his')
  
  
#Mean values of all variables in the cluster

grouped = german_data.groupby('Cluster', as_index=False)['age', 'duration', 'amount', 'response'].mean().round(2)
print(grouped)

warnings.filterwarnings('ignore')


#Targetable customer base

grouped2 = german_data.groupby(['Cluster','purpose'], as_index=False)['amount','response'].agg(['mean','count'])

grouped3 = grouped2.reset_index()
grouped3.columns = ['Cluster', 'Purpose', 'Mean_Amount','Count', 'Mean_Response', 'Count_Response']
grouped4 = grouped3[['Cluster', 'Purpose', 'Mean_Amount','Count', 'Mean_Response']]
grouped4.head()


fig5 = px.scatter(grouped4, x="Mean_Response", y="Mean_Amount", size="Count", color="Cluster",
                 hover_name="Purpose", size_max=60)
fig5.update_layout(height=600, width=1000, title_text="Credit Worthiness of each segment")
warnings.filterwarnings('ignore')
fig5.show()
