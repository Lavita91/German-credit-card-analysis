#Defining a function to create plot

def get_df(data):
    out = data.value_counts(normalize=True).reset_index()
    return(out)

def plot(x):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=get_df(cluster0[x])['index'],
        y=get_df(cluster0[x])[x],
        name='Cluster 0',
        marker_color='mediumaquamarine'
    ))
    fig.add_trace(go.Bar(
        x=get_df(cluster1[x])['index'],
        y=get_df(cluster1[x])[x],
        name='Cluster 1',
        marker_color='steelblue'
    ))
    fig.add_trace(go.Bar(
        x=get_df(cluster2[x])['index'],
        y=get_df(cluster2[x])[x],
        name='Cluster 2',
        marker_color='sandybrown'
    ))
    fig.add_trace(go.Bar(
        x=get_df(cluster3[x])['index'],
        y=get_df(cluster3[x])[x],
        name='Cluster 3',
        marker_color='indianred'
    ))

    fig.update_layout(barmode='group', xaxis_tickangle=45, title=x)
    fig.show()
    
    
    plot('saving_acct')
    plot('installment_rate')
    plot('housing')
    plot('n_credits')
    plot('job')
    plot('present_emp')
    plot('sex')
    plot('credit_his')
