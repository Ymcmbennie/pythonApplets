import folium
import os
import json

#create a map

m = folium.Map(location=[41.033965,29.228986], zoom_start=12)

# Global tooltip
tooltip = 'BensonAD Headquarters'

#creating custom marker icon
logoicon = folium.features.CustomIcon('icon.png', icon_size = (30, 30))

#Vega dat import for plotting 
vis = os.path.join('Data', 'vis.json')

#Geojson data  import for plotting 
overlay = os.path.join('Data', 'overlay.json')

# Create a marker
folium.Marker([41.033965,29.228986], 
                popup='<strong>BensonAD Offices</strong>',
                tooltip=tooltip).add_to(m),
#changing icon
folium.Marker([41.011997,29.155631], 
                popup='<strong>BensonAD Servers</strong>',
                tooltip=tooltip,
                icon=folium.Icon(icon='cloud')).add_to(m), 
#changing color
folium.Marker([41.003707,29.192008], 
                popup='<strong>BensonAD Secondary servers</strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m),                  
#changing color and icon, you can use material icons
folium.Marker([41.008111,29.218776], 
                popup='<strong>BensonAD Waste facilities</strong>',
                tooltip=tooltip,
                icon=folium.Icon(color='purple')).add_to(m), 
#with custom logo
folium.Marker([41.015883,29.234219],
              popup='<strong>BensonAD master</strong>',
              tooltip=tooltip,
              icon=logoicon).add_to(m),

#New vega marker
folium.Marker([41.009241,29.237917], 
                popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450,height=250))).add_to(m), 

#geojson overlay
folium.GeoJson(overlay, name='cambridge').add_to(m)

#generate circle marker for areas
folium.CircleMarker(
    location=[41.021412,29.219159],
    radius=50,
    popup="My site area",
    color='#428bca',
    fill= True,
    fill_color = '#428bca'
).add_to(m),
# Generate Map
m.save('map.html')