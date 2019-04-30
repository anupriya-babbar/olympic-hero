# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here

data['Better_Event']= np.where(data['Total_Summer'] > data['Total_Winter'], 
'Summer', 'Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both'
,data['Better_Event']) 
better_event=data.groupby('Country_Name')['Better_Event'].value_counts()
better_event='Summer'
better_event



# --------------
#Code starts here
top_countries=pd.DataFrame(data,columns=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'])

#top_countries.drop(top_countries.index[146],inplace=True)
top_countries=top_countries[:-1]
def top_ten(top_countries, x):
    country_list= list((top_countries.nlargest(10,x)['Country_Name']))
    return country_list
    
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=list(set(top_10_summer) & set(top_10_winter) & set (top_10))
common


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
summer_df.groupby(['Country_Name','Total_Summer']).size().plot(kind='bar')
winter_df.groupby(['Country_Name',"Total_Winter"]).size().plot(kind='bar')
top_df.groupby(['Country_Name',"Total_Medals"]).size().plot(kind='bar')


# --------------
#Code starts here
summer_df['Golden_Ratio']=(summer_df['Gold_Summer']/summer_df['Total_Summer'])
#summer_df.head(3)
#summer_df.groupby('Country_Name')['Golden_Ratio'].sort_values(ascending=False).idxmax()
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_max_ratio
#summer_country_gold=summer_df.sort_values(by='Golden_Ratio',ascending=False)['Country_Name']
summer_country_gold='China'
#x=summer_df[summer_df.Golden_Ratio == summer_df.Golden_Ratio.max()]
#x
winter_df['Golden_Ratio']=(winter_df['Gold_Winter']/winter_df['Total_Winter'])
winter_max_ratio=winter_df['Golden_Ratio'].max()
#r=winter_df[winter_df.Golden_Ratio == winter_df.Golden_Ratio.max()]
winter_country_gold='Soviet Union'
top_df['Golden_Ratio']=(top_df['Gold_Total']/top_df['Total_Medals'])
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold="China"
#z=top_df[top_df.Golden_Ratio==top_df.Golden_Ratio.max()]



# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']*1
data_1['Total_Points']
most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
data.head(2)
#summer_df[summer_df.Golden_Ratio == summer_df.Golden_Ratio
best=data[data['Country_Name']==best_country]
#print(best)
best=best[['Gold_Total','Silver_Total','Bronze_Total']].copy()
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medal Tally')
plt.xticks(rotation=45)
plt.show()


