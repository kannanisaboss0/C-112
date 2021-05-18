#-----------------------------------------------------------GoldData19502021.py-----------------------------------------------------------#
'''
Importing modules:
-pandas (pd)
-plotly.figure_factory (ff)
-plotly.express (px)
-plotlygraph_objects (go)
-statistics (st)
-random (rd)
-numpy (np)
-time (tm)
'''

import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import statistics as st 
import random as rd
import numpy as np 
import time as tm


#Defining a function to request the user for comparing
def RequestUserForComparison():
  input_param=input("Should the data be abstracted on the basis of price?(:-Yes or No)")

  #Assessing the user's input on abstraction of the price
  #Case-1
  if(input_param=="Yes"or input_param=="yes"):
    return "Yes"
  #Case-2  
  else:
    return "No"  


#Defining a function to assess the user's choice
def AssessUserChoiceForComparison(df_yearly,interval_choice):

  method_list=["Unusable_Element","The value should be greater","The value should be lesser"]
  method_count=0

  for method in method_list[1:]:
    method_count+=1
    print(str(method_count)+":"+method)

  user_input_param=int(input("Please enter the index of the method by which the data should be abstracted according to the aforementioned list"))
  
  choice_param=method_list[1]

  #Checking the user's input to call the the accurate function
  #Case-1
  if(user_input_param==1):
    AbstractDataFromDataFrame(df_yearly,"Greater",interval_choice)
  #Case-2
  elif(user_input_param==2):
    AbstractDataFromDataFrame(df_yearly,"Lesser",interval_choice)


#Defining a function which abstracts the dataframe according to the method and value
def AbstractDataFromDataFrame(df_arg,abstractive_method,label_arg):

  value_param=int(input("Please enter the value to be compared and to abstract the dataframe:"))

  #Assessing the abstraction using the parameter given from the previous function
  #Case-1
  if(abstractive_method=="Greater"):
    df_loc_greater=df_arg.loc[df_arg["Price"]>value_param]
    df_list=df_loc_greater["Price"].tolist()

    #Checking the validity of the abstracted list
    #Case-1
    if(len(df_list)>1):
      CalculateMeanMedianAndStandardDeviationOfData(df_loc_greater,label_arg,df_list)
    #Case-2
    else:

      #Prinintg the enidng message
      print("Request Terminated")
      print("Invalid Comparitive Value")
      print("Thank you for GoldData19502021.py")
  #Case-2
  if(abstractive_method=="Lesser"):
    df_loc_lesser=df_arg.loc[df_arg["Price"]<value_param]
    df_list=df_loc_lesser["Price"].tolist()

    #Checking the validity of the abstracted list
    #Case-1
    if(len(df_list)>1):
      CalculateMeanMedianAndStandardDeviationOfData(df_loc_lesser,label_arg,df_list)

    #Case-2
    else:

      #Prinintg the enidng message
      print("Request Terminated")
      print("Invalid Comparitive Value")
      print("Thank you for GoldData19502020.py")

#Defining a function to calculate the mean,median and standard deviation of the data
def CalculateMeanMedianAndStandardDeviationOfData(df_arg,label_arg,df_list_arg):

  mean_param=st.mean(df_list_arg)
  median_param=st.median(df_list_arg)
  st_dev_param=st.stdev(df_list_arg)

  CreateLineBarAndScatterGraphsFromData(df_arg,label_arg,df_list_arg,mean_param,median_param,st_dev_param)

#Defining a function to create line,bar and scatter graphs using datafrom the dataset
def CreateLineBarAndScatterGraphsFromData(df_arg,label_arg,df_list_arg,mean_arg,median_arg,st_dev_arg):

  line_graph=px.line(df_arg,x="Date",y="Price",title="Gold Prices(1950-2021):"+label_arg+":-Line Graph")

  if(label_arg=="Yearly Interval"):
    line_graph.update_traces(mode="markers+lines")

  line_graph.show()

  bar_graph=px.bar(df_arg,x="Date",y="Price",title="Gold Prices(1950-2021):"+label_arg+":-Bar Graph")
  bar_graph.show()

  scatter_graph=px.scatter(df_arg,x="Date",y="Price",title="Gold Prices(1950-2021):"+label_arg+":-Scatter Graph")
  scatter_graph.show()

  print("The mean value of the prices is {}".format(mean_arg))
  print("The median value of the prices is {}".format(median_arg))
  print("The standard deviation value of the prices is {}".format(st_dev_arg))

  CreateDistributionPlotAndCalculateStandardDeviationsFromData(df_list_arg,label_arg)


#Defining a function to create a distribution plot using the data given from the dataset
def CreateDistributionPlotAndCalculateStandardDeviationsFromData(df_list_arg,label_arg):

  mean_param=st.mean(df_list_arg)
  st_dev_param=st.stdev(df_list_arg)
  median_param=st.median(df_list_arg)

  st_dev_1_start,st_dev_1_end=mean_param-(1*st_dev_param),mean_param+(1*st_dev_param)
  st_dev_2_start,st_dev_2_end=mean_param-(2*st_dev_param),mean_param+(2*st_dev_param)
  st_dev_3_start,st_dev_3_end=mean_param-(3*st_dev_param),mean_param+(3*st_dev_param)

  dist_plot=ff.create_distplot([df_list_arg],["Gold Prices(1950-2021):"+label_arg+":-Distribution Plot(Original Data)"],show_hist=False,curve_type='normal')

  dist_plot.add_trace(go.Scatter(x=[st_dev_1_start,st_dev_1_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_2_start,st_dev_2_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_3_start,st_dev_3_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  dist_plot.add_trace(go.Scatter(x=[st_dev_1_end,st_dev_1_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_2_end,st_dev_2_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_3_end,st_dev_3_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  dist_plot.add_trace(go.Scatter(x=[mean_param,mean_param],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Mean Value"))

  dist_plot.update_layout(title="Gold Prices(1950-2021):"+label_arg+":-Distribution Plot(Original Data)")

  dist_plot.show()

  percentage_1=[value for value in df_list_arg if st_dev_1_start<value<st_dev_1_end]
  percentage_2=[value for value in df_list_arg if st_dev_2_start<value<st_dev_2_end]
  percentage_3=[value for value in df_list_arg if st_dev_3_start<value<st_dev_3_end]

  print("Population Data:")

  print("{}% of data lies between the first standard deviation".format(round((len(percentage_1*100)/len(df_list_arg)),2)))
  print("{}% of data lies between the second standard deviation".format(round((len(percentage_2*100)/len(df_list_arg)),2)))
  print("{}% of data lies between the third standard deviation".format(round((len(percentage_3*100)/len(df_list_arg)),2)))

  print("The mean value of the population is {}".format(round(mean_param,2)))
  print("The median value of the population is {}".format(round(median_param,2)))
  print("The standard deviation value of the population is {}".format(round(st_dev_param,2)))

  CreateDistributionPlotAndCalculateStandardDeviationsFromDataForSampleData(df_list_arg,label_arg)
 

#Defining a function to create a distribution for the first set of sample data
def CreateDistributionPlotAndCalculateStandardDeviationsFromDataForSampleData(df_list_arg,label_arg):

  final_list=[]

  for loop in range(1000):
    mean_list=[]

    for value in range(100):
      random_index=rd.randint(0,(len(df_list_arg)-1))
      mean_list.append(df_list_arg[random_index])

    mean_list_mean=st.mean(mean_list)
    final_list.append(mean_list_mean)  

      
  mean_param=st.mean(final_list)
  st_dev_param=st.stdev(final_list)
  median_param=st.median(final_list)

  st_dev_1_start,st_dev_1_end=mean_param-(1*st_dev_param),mean_param+(1*st_dev_param)
  st_dev_2_start,st_dev_2_end=mean_param-(2*st_dev_param),mean_param+(2*st_dev_param)
  st_dev_3_start,st_dev_3_end=mean_param-(3*st_dev_param),mean_param+(3*st_dev_param)

  dist_plot=ff.create_distplot([final_list],["Gold Prices(1950-2021):"+label_arg+":-Distribution Plot(Sample Data)"],show_hist=False,curve_type='normal')

  dist_plot.add_trace(go.Scatter(x=[st_dev_1_start,st_dev_1_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_2_start,st_dev_2_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_3_start,st_dev_3_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  dist_plot.add_trace(go.Scatter(x=[st_dev_1_end,st_dev_1_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_2_end,st_dev_2_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_3_end,st_dev_3_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  dist_plot.add_trace(go.Scatter(x=[mean_param,mean_param],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Mean Value"))

  dist_plot.update_layout(title="Gold Prices(1950-2021):"+label_arg+":-Distribution Plot(Sample Data) 1/2")

  dist_plot.show()

  percentage_1=[value for value in final_list if st_dev_1_start<value<st_dev_1_end]
  percentage_2=[value for value in final_list if st_dev_2_start<value<st_dev_2_end]
  percentage_3=[value for value in final_list if st_dev_3_start<value<st_dev_3_end]

  print("First Sample Data:")

  print("{}% of data lies between the first standard deviation".format(round((len(percentage_1*100)/len(final_list)),2)))
  print("{}% of data lies between the second standard deviation".format(round((len(percentage_2*100)/len(final_list)),2)))
  print("{}% of data lies between the third standard deviation".format(round((len(percentage_3*100)/len(final_list)),2)))

  print("The mean value of the sample is {}".format(round(mean_param,2)))
  print("The median value of the sample is {}".format(round(median_param,2)))
  print("The standard deviation value of the sample is {}".format(round(st_dev_param,2)))

  CreateDistributionPlotAndCalculateStandardDeviationsFromDataForSampleData2(df_list_arg,label_arg,final_list)


#Defining a function to create a distribution plot for the second set of sample data
def CreateDistributionPlotAndCalculateStandardDeviationsFromDataForSampleData2(df_list_arg,label_arg,sample_1_arg):

  final_list=[]

  for loop in range(1000):
    mean_list=[]

    for value in range(100):
      random_index=rd.randint(0,(len(df_list_arg)-1))
      mean_list.append(df_list_arg[random_index])

    mean_list_mean=st.mean(mean_list)
    final_list.append(mean_list_mean)  
    median_param=st.median(final_list)

  mean_param=st.mean(final_list)
  st_dev_param=st.stdev(final_list)

  st_dev_1_start,st_dev_1_end=mean_param-(1*st_dev_param),mean_param+(1*st_dev_param)
  st_dev_2_start,st_dev_2_end=mean_param-(2*st_dev_param),mean_param+(2*st_dev_param)
  st_dev_3_start,st_dev_3_end=mean_param-(3*st_dev_param),mean_param+(3*st_dev_param)

  dist_plot=ff.create_distplot([final_list],["Gold Prices(1950-2021):"+label_arg+":-Distribution Plot(Sample Data)"],show_hist=False,curve_type='normal')

  dist_plot.add_trace(go.Scatter(x=[st_dev_1_start,st_dev_1_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_2_start,st_dev_2_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_3_start,st_dev_3_start],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  dist_plot.add_trace(go.Scatter(x=[st_dev_1_end,st_dev_1_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 1"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_2_end,st_dev_2_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 2"))
  dist_plot.add_trace(go.Scatter(x=[st_dev_3_end,st_dev_3_end],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Standard Deviation 3"))

  dist_plot.add_trace(go.Scatter(x=[mean_param,mean_param],y=[0,max(dist_plot["data"][0]["y"])],mode="lines",name="Mean Value"))

  dist_plot.update_layout(title="Gold Prices(1950-2021):"+label_arg+":-Distribution Plot(Sample Data) 2/2")

  dist_plot.show()

  percentage_1=[value for value in final_list if st_dev_1_start<value<st_dev_1_end]
  percentage_2=[value for value in final_list if st_dev_2_start<value<st_dev_2_end]
  percentage_3=[value for value in final_list if st_dev_3_start<value<st_dev_3_end]

  print("Second Sample Data:")

  print("{}% of data lies between the first standard deviation".format(round((len(percentage_1*100)/len(final_list)),2)))
  print("{}% of data lies between the second standard deviation".format(round((len(percentage_2*100)/len(final_list)),2)))
  print("{}% of data lies between the third standard deviation".format(round((len(percentage_3*100)/len(final_list)),2)))

  print("The mean value of the first sample is {}".format(round(mean_param,2)))
  print("The median value of the sample is {}".format(round(median_param,2)))
  print("The standard deviation value of the sample is {}".format(round(st_dev_param,2)))

  CalculateCorrelationBetweenSampleData(final_list,sample_1_arg,df_list_arg)  


#Defining a function to calculate the correlation between the the first and second ssets of sample data
def CalculateCorrelationBetweenSampleData(sample_list_2_arg,sample_list_1_arg,df_list_arg):

  dict_object_param={"x":sample_list_1_arg,"y":sample_list_2_arg}

  correlation_1=np.corrcoef(dict_object_param["x"],dict_object_param["y"])
  correlation_2=np.corrcoef(dict_object_param["y"],dict_object_param["x"])

  print("Common Sample Data:")

  print("The correlative coefficient between the first sample and second sample is {}".format(round(correlation_1[0,1],2)))
  print("The correlative coefficient between the second sample and first sample is {}".format(round(correlation_2[0,1],2)))

  CalculateZSampleTests(df_list_arg,sample_list_1_arg,sample_list_2_arg)


#Defining a function to calculate the Z-Sample tests for teh first and secondd sets of sammple data  
def CalculateZSampleTests(original_list_arg,sample_list_1_arg,sample_list_2_arg):

  original_list_mean,sample_list_1_mean,sample_list_2_mean=st.mean(original_list_arg),st.mean(sample_list_1_arg),st.mean(sample_list_2_arg)
  sample_list_1_st_dev,sample_list_2_st_dev=st.stdev(sample_list_1_arg),st.stdev(sample_list_2_arg)

  z_sample_1=(original_list_mean-sample_list_1_mean)/sample_list_1_st_dev
  z_sample_2=(original_list_mean-sample_list_2_mean)/sample_list_2_st_dev

  print("The Z-Sample of the first sample is {}".format(round(z_sample_1,2)))
  print("The Z-Sample of the second sample is {}".format(round(z_sample_2,2)))
  
  #Printing the ending message
  PrintEndingMessage()


#Defining a function to print the ending message
def PrintEndingMessage():
  print("Thank you for using GoldData19502021.py")


#Introductory statement and user input
print("Welcome to GoldData195020201.py. We provide the price of one unit of gold gloablly in USD.")
print("Loading data...")
tm.sleep(1.3)

interval_list=["Unusable_Element","Monthly Interval","Yearly Interval"]
interval_count=0

for interval_unit in interval_list[1:]:
  interval_count+=1
  print("{}:{}".format(interval_count,interval_unit))

user_input=int(input("Please enter the index of the  time interval of the data desired to visually represent:"))  
interval_choice=interval_list[user_input]

#Assessing the user's input to fetch the correct dataset
#Case-1
if(user_input==1):
  df_monthly=pd.read_csv("data.csv")
  df_monthly_list=df_monthly["Price"].tolist()

  #Requesting the user for comparison of values
  #Case-1
  if(RequestUserForComparison()=="Yes"):
    AssessUserChoiceForComparison(df_monthly,interval_choice)
  #Case-2
  else:
    CalculateMeanMedianAndStandardDeviationOfData(df_monthly,interval_choice,df_monthly_list)
#Case-2
elif(user_input==2):
  df_yearly=pd.read_csv("data_2.csv")
  df_yearly_list=df_yearly["Price"].tolist()

  #Requesting the user for comparison of values
  #Case-1
  if(RequestUserForComparison()=="Yes"):
    AssessUserChoiceForComparison(df_yearly,interval_choice)
  #Case-2
  else:
    CalculateMeanMedianAndStandardDeviationOfData(df_yearly,interval_choice,df_yearly_list)
#-----------------------------------------------------------GoldData19502021.py-----------------------------------------------------------#

  
     

  


