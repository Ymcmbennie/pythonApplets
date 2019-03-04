import folium
import os
import json

# create a map

m = folium.Map(location=[51.800420, 19.751590], zoom_start=14)

# Global tooltip
tooltip = 'Click for more info'

# creating custom marker icon
logoicon = folium.features.CustomIcon('icon.png', icon_size=(30, 30))

# Vega dat import for plotting
vis = os.path.join('Data', 'vis.json')

# Geojson data  import for plotting
overlay = os.path.join('Data', 'overlay.json')

# Create a marker
folium.Marker([51.800457, 19.751624],
              popup='<strong>Main Square</strong>',
              tooltip=tooltip).add_to(m),
# changing icon
folium.Marker([51.801496, 19.741710],
              popup='<strong>Old catholic church</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
# changing color
folium.Marker([51.800442, 19.741431],
              popup='<strong>Green park and Pond</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m),
# changing color and icon, you can use material icons
folium.Marker([51.800442, 19.741231],
              popup='<strong>BensonAD Waste facilities</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
# with custom logo
folium.Marker([51.800442, 19.741331],
              popup='<strong>BensonAD master</strong>',
              tooltip=tooltip,
              icon=logoicon).add_to(m),

# New vega marker
folium.Marker([51.800442, 19.741531],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m),

# geojson overlay
folium.GeoJson(overlay, name='cambridge').add_to(m)

# generate circle marker for areas
folium.CircleMarker(
    location=[51.800457, 19.751624],
    radius=50,
    popup="My site area",
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m),
# Generate Map
m.save('map.html')
