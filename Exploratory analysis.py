german_data[["amount", "duration", "age"]].describe().round(2)

#Distribution Plots

fig = make_subplots(rows=1, cols=3)

trace0 = go.Histogram(x=german_data["amount"], name='Credit Amount Distribution')
trace1 = go.Histogram(x=german_data["duration"], name="Duration Distribution")
trace2 = go.Histogram(x=german_data["age"], name="Age Distribution")

fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,2)
fig.append_trace(trace2,1,3)

#Updating xaxes and yaxes

fig.update_xaxes(title_text="Credit Amount", row=1, col=1)
fig.update_xaxes(title_text="Duration", row=1, col=2)
fig.update_xaxes(title_text="Age", row=1, col=3)

fig.update_yaxes(title_text="Count", row=1, col=1)

fig.update_layout(height=500, width=1000, title_text="Distribution Plots")
fig.show()

#Distribution of credit amount across various reasons 

fig2 = px.box(german_data, x="purpose", y="amount", color="response", title="Distribution of credit amount across various reasons")

fig2.update_layout(height=500, width=1000)
fig2.show()

#Scatter plots
import plotly.figure_factory as ff

fig3 = ff.create_scatterplotmatrix(german_data[['age','duration','amount']], diag='box', 
                                   #index='index',
                                   colormap='Portland',colormap_type='cat',height=700, width=700)
fig3.show()
