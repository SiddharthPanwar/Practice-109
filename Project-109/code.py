import random
import pandas as pd
from re import X
import plotly.figure_factory as px
import statistics
import plotly.graph_objects as go
data = pd.read_csv("data.csv")
mean = sum(data)/len(data)
print("Mean of the data is" ,mean)
median = statistics.median(data)
print("Median of the dataset is : ", median)
mode = statistics.mode(data)
print("Mode of your data is : ", mode)
stdev = statistics.stdev(data)
print("The standard Deviation of your data is : ",stdev)
fig = px.create_distplot([data],["Result"] )
first_standard_deviation_start,first_standard_deviation_end = mean-stdev,mean+stdev
second_standard_deviation_start,second_standard_deviation_end = mean-2*stdev,mean+2*stdev
third_standard_deviation_start,third_standard_deviation_end = mean-3*stdev,mean+3*stdev
listofdata_within_first_standard_deviation = [result for result in data if result>first_standard_deviation_start and result<first_standard_deviation_end]
listofdata_within_second_standard_deviation = [result for result in data if result>second_standard_deviation_start and result<second_standard_deviation_end]
listofdata_within_third_standard_deviation = [result for result in data if result>third_standard_deviation_start and result<third_standard_deviation_end]
print("{}% of data lies within first standard deviation".format(len(listofdata_within_first_standard_deviation)*100/len(data)))
print("{}% of data lies within second standard deviation".format(len(listofdata_within_second_standard_deviation)*100/len(data)))
print("{}% of data lies within third standard deviation".format(len(listofdata_within_third_standard_deviation)*100/len(data)))
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_start,first_standard_deviation_start],y=[0,0.17],mode="lines",name="first standard deviation"))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end,first_standard_deviation_end],y=[0,0.17],mode="lines",name="first standard deviation"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_start,second_standard_deviation_start],y=[0,0.17],mode="lines",name="second standard deviation"))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end,second_standard_deviation_end],y=[0,0.17],mode="lines",name="second standard deviation"))
fig.show()