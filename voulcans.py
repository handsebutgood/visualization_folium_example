#Import Library
import folium
from folium.plugins import MarkerCluster
import pandas as pd

#Load Data
data = pd.read_csv("data/Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles= "CartoDB dark_matter")

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#Plot Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon],
                        popup=str(elevation)+" m",
                        radius=9,
                        fill_color = color_change(elevation), fill_opacity=0.9).add_to(map).add_to(marker_cluster)

#Save the map
map.save("voulcan.html")