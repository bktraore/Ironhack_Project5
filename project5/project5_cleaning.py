# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 22:25:33 2022

@author: kyrie
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#scatter chart plotly
import plotly.express as px

color = sns.color_palette("viridis")


df = pd.read_csv(r"C:\Users\kyrie\ironhack\project5\clean_data_project5.csv")


dfcolumns = df.columns
daycount = df['weekday'].value_counts()
df['managerVehicle']= df['managerVehicle'].replace(1,'Yes')
df['managerVehicle']= df['managerVehicle'].replace(0,'No')

import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)



### Title of the page
st.markdown(
	"<h1 style='text-align: center;'>Project 5</h1>",
	unsafe_allow_html=True,
)

from PIL import Image
image = Image.open(r"C:\Users\kyrie\Downloads\carr.jpg")
#center the image in the middle of the page
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(image, use_column_width=True)

###################################################################################
## SECTION 1
st.markdown("## Charger Type")

# filter the data for
clist = df["facilityType"].unique()
st.sidebar.markdown("## charger Type: ")
facilityType = st.sidebar.selectbox("Select a facility Type: ", clist)
filter1 = df[df["facilityType"] == facilityType]


########## METRICS INDICATORS
m1, m2, m3, m4 = st.columns((1, 1, 1, 1))
mean_payments = round(filter1["dollars"].mean(), 1)
mean_kwh = round(filter1["kwhTotal"].mean(), 1)
mean_charging_times = round(filter1["chargeTimeHrs"].mean(), 1)
facilityType_count = filter1["facilityType"].count()

m1.metric(label="facilty Type count", value=facilityType_count)
m2.metric(label="average payment", value=str(float(mean_payments)) + " $")
m3.metric(label="average kwh", value=str(float(mean_kwh)) + " Kwh")
m4.metric(label="Average charging time", value=str(float(mean_charging_times)) + " Hours")


## SECTION 2
st.sidebar.markdown("Payment Platform")
st.markdown("## Payment Platform")

# filter the data for
clist = df["platform"].unique()
platform = st.sidebar.selectbox("Select a platform: ", clist)
filter2 = df[df["platform"] == platform]


########## METRICS INDICATORS
mm1, mm2, mm3, mm4 = st.columns((1, 1, 1, 1))
mean_payments = round(filter2["dollars"].mean(), 1)
mean_kwh = round(filter2["kwhTotal"].mean(), 1)
mean_charging_times = round(filter2["chargeTimeHrs"].mean(), 1)
platform_count = filter2["platform"].count()

mm1.metric(label="platform", value=platform_count)
mm2.metric(label="average payment", value=str(float(mean_payments)) + " $")
mm3.metric(label="average kwh", value=str(float(mean_kwh)) + " Kwh")
mm4.metric(label="Average charging time", value=str(float(mean_charging_times)) + " Hours")

#####################################################################

st.markdown("## day of Charging")

dfpie = pd.DataFrame({'day': ['Fri','Mon','Sat','Sun','Thu','tue','Wed'], 'count': [610, 615, 62, 24,735,635,713]},
                      index = [1, 2, 3, 4, 5, 6, 7])
fig18 = px.pie(dfpie, values='count', names='day', color_discrete_sequence=px.colors.sequential.Viridis)
st.plotly_chart(fig18)
#############

df['index_col'] = df.index

choix = st.sidebar.selectbox("Select one variable to heatmap", ['price', 'kwh_Total','charging_Hour'])

if choix == "price":
    st.title("heatmap of the price distribution")
    fig5 = px.density_heatmap(
    data_frame=df, y="index_col", x="dollars"
    )
    st.plotly_chart(fig5)
    
if choix == "kwh_Total":
    fig6 = px.density_heatmap(
    data_frame=df, y="index_col", x="kwhTotal"
    )
    st.plotly_chart(fig6)
    
if choix == 'charging_Hour':
    st.title("heatmap of the price distribution")
    fig7 = px.density_heatmap(
    data_frame=df, y="index_col", x="startTime"
    )
    st.plotly_chart(fig7)




## SECTION 3

st.markdown("## additional Bar chart of the charge time, the price and the electricity quantity")

chart_data = pd.DataFrame(
    df[['chargeTimeHrs','kwhTotal', 'dollars']].head(60),
    columns=["chargeTimeHrs", "kwhTotal", "dollars"])
st.bar_chart(chart_data)




#df['weekday'].value_counts().index




#create two columns with the two scatter plots
fig_col1, fig_col2 = st.columns(2)

df['col3'] = np.arange(len(df))*0.05

with fig_col1:
    st.markdown(
    	"<h2 style='text-align: center;'>charge time depending on the charger type</h2>",
    	unsafe_allow_html=True,
    )
    fig3 = px.scatter(df, x='facilityType', y='chargeTimeHrs',size = 'col3')  
    st.plotly_chart(fig3)


with fig_col2:
    st.markdown(
    	"<h2 style='text-align: center;'>price depending on the charge time</h2>",
    	unsafe_allow_html=True,
    )
    fig2 = px.scatter(df, x='dollars', y='chargeTimeHrs', size ='col3')  
    st.plotly_chart(fig2)

    


manager_unique = df['managerVehicle'].unique()
filtre = st.sidebar.selectbox("Manager Vehicle ? ", manager_unique)
manager =  df[df['managerVehicle']== filtre]

#pi = manager.groupby(['facilityType'])['managerVehicle'].count()

label = ['Type 1','Type 2','Type 3','Type 4']
y = manager.groupby(['facilityType'])['managerVehicle'].count()
#plt.style.use('seaborn-colorblind')
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=label, colors = color, autopct='%1.0f%%')
plt.title('repartiton of the charger Type')




st.pyplot()






    
    
