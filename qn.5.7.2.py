import numpy as np 
import pandas as pd 
import geohash2
from folium.plugins import HeatMap
import folium
import re

df = pd.read_csv('d:/1.csv',usecols=['starttime','geohashed_start_loc','geohashed_end_loc'])
df_start = pd.DataFrame()
df_end = pd.DataFrame()
df = df[180000:230000]

for i in range(df.shape[0]):
    an = re.search('2017-05-10\s07:\d\d:\d\d',df.iloc[i,0])#2017-05-(10|11|12|15|16|17|18|19|22|23)\s(06|07|08):\d\d:\d\d
    if(an):
        df_start = df_start.append([geohash2.decode(df.iloc[i][1])],ignore_index = True)
        df_end = df_end.append([geohash2.decode(df.iloc[i][2])],ignore_index = True)




lis_start = []
lis_end = []
for j in range(df_start.shape[0]):
    lis_start.append([df_start.iloc[j][0],df_start.iloc[j][1],1])

for k in range(df_end.shape[0]):
    lis_end.append([df_end.iloc[k][0],df_end.iloc[k][1],1])
    



city_map_start = folium.Map(
    location=[39.93, 116.38],
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
    attr="default"
    )
HeatMap(lis_start).add_to(city_map_start)
city_map_start.save('D:/map_start.html')

city_map_end = folium.Map(
    location=[39.93, 116.38],
    zoom_start=15,
    tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
    attr="default"
    )
HeatMap(lis_end).add_to(city_map_end)
city_map_end.save('D:/map_end.html1')



