import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

#to read data in data frames
df=pd.read_csv("data.csv")

#converting data in list(array)
height=df['Height'].tolist()

#1mean mode median will be equal
mean=statistics.mean(height)
median=statistics.median(height)
mode=statistics.mode(height)
print("mean=",mean)
print("median=",median)
print("mode=",mode)


#calculating sd
sd=statistics.stdev(height)
print("sd=",sd)
#1st Sd = 68% 2nd 90%,3rd 100%
#1st ,2nd , 3rd sd
FSDS,FSDE=mean-sd,mean+sd
SSDS,SSDE=mean-(2*sd),mean+(2*sd)
TSDS,TSDE=mean-(3*sd),mean+(3*sd)

#percentage of sd in FSD,SSD,TSD
inFSD=[i for i in height if i> FSDS and i<FSDE]
inSSD=[i for i in height if i>SSDS and i< SSDE]
inTSD=[i for i in height if i>TSDS and i< TSDE]

#lets print the percentage
print("{}% of data for height lies within 1 standard deviation".format(len(inFSD)*100.0/len(height)))
print("{}% of data for height lies within 2 standard deviation".format(len(inSSD)*100.0/len(height)))
print("{}% of data for height lies within 3 standard deviation".format(len(inTSD)*100.0/len(height)))




#graph
fig=ff.create_distplot([height],["height"],show_hist=False)
#mean ploting FIRST Standard deviation start  FSDS,  FIRST Standard deviationstart end FSDE 
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[TSDS,TSDS],y=[0,0.17],mode="lines",name="TSDS"))
fig.add_trace(go.Scatter(x=[TSDE,TSDE],y=[0,0.17],mode="lines",name="TSDE"))
#FSD ploting 

fig.show()


