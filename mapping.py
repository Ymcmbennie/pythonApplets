import folium
import os
import json

# create a map

m = folium.Map(location=[51.764980, 19.451964], zoom_start=17)

# Global tooltip
tooltip = 'Click for more info'


# creating custom marker icon
logoicon = folium.features.CustomIcon('icon.png', icon_size=(30, 30))

# Vega dat import for plotting
vis = os.path.join('Data', 'vis.json')

# Geojson data  import for plotting
overlay = os.path.join('Data', 'overlay.json')
overlay1 = os.path.join('Data', 'overlay1.json')
overlay2 = os.path.join('Data', 'overlay2.json')
overlay3 = os.path.join('Data', 'overlay3.json')
overlay4 = os.path.join('Data', 'overlay4.json')

# Create a marker
folium.Marker([51.757241, 19.406272],
              popup='<strong>Main Square</strong>',
              tooltip=tooltip).add_to(m),

folium.Marker([51.760028, 19.408994],
              popup='<strong>Main Square</strong>',
              tooltip=tooltip).add_to(m),

folium.Marker([51.754116, 19.403152],
              popup='<strong>Main Square</strong>',
              tooltip=tooltip).add_to(m),

folium.Marker([51.757304, 19.400233],
              popup='<strong>Main Square</strong>',
              tooltip=tooltip).add_to(m),

# changing icon
folium.Marker([51.765205, 19.452695],
              popup='<div ><img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Ulica_Andrzeja_Struga_Lodz.jpg" width="30"/></div>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
# changing color
folium.Marker([51.760973, 19.410779],
              popup='<strong>Green park and Pond</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),
# changing color and icon, you can use material icons
folium.Marker([51.758203, 19.413531],
              popup='<strong>Stop</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
# with custom logo
folium.Marker([51.760159, 19.403417],
              popup='<strong>BensonAD master</strong>',
              tooltip=tooltip,
              icon=logoicon).add_to(m),

# New vega marker
folium.Marker([51.754750, 19.411785],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m),

# geojson overlay
folium.GeoJson(overlay, 
    name='Site Design', 
    tooltip='Main Site'
    ).add_to(m)
folium.GeoJson(overlay1, name='Site1 Design', tooltip='Small Green Space').add_to(m)
folium.GeoJson(overlay2, name='Site2 Design', tooltip='Small Green Space').add_to(m)
folium.GeoJson(overlay3, name='Site3 Design', tooltip='Small Green Space').add_to(m)
folium.GeoJson(overlay4, name='Site4 the rest Design', tooltip='Small Potential Space').add_to(m)


# generate circle marker for areas
folium.CircleMarker(
    location=[51.764988, 19.451949],
    radius=10,
    popup="My site area",
    color='#660707',
    fill=True,
    fill_color='#bc0d0d'
).add_to(m),
# Generate Map
m.save('map.html')
