import folium
import os
import json

# create a map

m = folium.Map(location=[51.776639, 19.454855], zoom_start=13)

# Global tooltip
tooltip = 'Click for more info'

# creating custom marker icon
logoicon = folium.features.CustomIcon('icon.png', icon_size=(30, 30))

# Vega dat import for plotting
vis = os.path.join('Data', 'vis.json')

# Geojson data  import for plotting
overlay0 = os.path.join('Data', 'overlay0.json')
'''
overlay1 = os.path.join('Data', 'overlay1.json')
overlay2 = os.path.join('Data', 'overlay2.json')
overlay3 = os.path.join('Data', 'overlay3.json')
overlay4 = os.path.join('Data', 'overlay4.json')
'''

def style_function(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'blue',
        'weight': 1.5
    }

# changing icon
folium.Marker([51.765205, 19.452695],
              popup='''<img src="/pics/20190330_104656.jpg" width="300">''',
              tooltip="Corner Small Green",
              icon=folium.Icon(icon='camera')).add_to(m),

folium.Marker([51.765100, 19.450280],
              popup='''<img src="/pics/20190330_105443.jpg" width="300">''',
              tooltip="Another small corner Gardern",
              icon=folium.Icon(icon='camera')).add_to(m),

folium.Marker([51.764365, 19.450267],
              popup='''<img src="/pics/20190330_105624.jpg" width="300">''',
              tooltip="Bigger corner Gardern",
              icon=folium.Icon(icon='camera')).add_to(m),

folium.Marker([51.764814, 19.452030],
              popup='''<img src="/pics/20190330_105851.jpg" width="300">''',
              tooltip="Main view of the plot from across the road",
              icon=folium.Icon(icon='camera')).add_to(m),

folium.Marker([51.759579, 19.458344],
              popup='''<img src="/pics/20190330_103348.jpg" width="300">''',
              tooltip="The big colorful station",
              icon=folium.Icon(icon='camera')).add_to(m),

folium.Marker([51.765570, 19.456988],
              popup='''<img src="/pics/20190330_104231.jpg" width="300">''',
              tooltip="Corner connection to main street",
              icon=folium.Icon(icon='camera')).add_to(m),

'''
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
'''
# geojson overlay
folium.GeoJson(overlay0, 
    name='Site Design', 
    style_function=lambda feature: {'fillColor': '#ff3300', 'color': '#ff3300', 'weight': 3},
    tooltip='Main Site'
    ).add_to(m)
'''
folium.GeoJson(overlay1, name='Site1 Design', 
    style_function=lambda feature: {'fillColor': '#00ff00', 'color': '#00ff00', 'weight': 2}, 
    tooltip='Small Green Space'
    ).add_to(m)
folium.GeoJson(overlay2, name='Site2 Design', 
    style_function=lambda feature: {'fillColor': '#00ff00', 'color': '#00ff00', 'weight': 2},
    tooltip='Small Green Space'
    ).add_to(m)
folium.GeoJson(overlay3, name='Site3 Design', 
    style_function=lambda feature: {'fillColor': '#00ff00', 'color': '#00ff00', 'weight': 2},
    tooltip='Small Green Space'
    ).add_to(m)
folium.GeoJson(overlay4, name='Site4 the rest Design', 
    style_function=lambda feature: {'fillColor': '#ffaf00', 'color': '#b38600', 'weight': 1},
    tooltip='Small Potential Space'
    ).add_to(m)


# generate circle marker for areas
folium.CircleMarker(
    location=[51.764988, 19.451949],
    radius=10,
    popup="My site area",
    color='#660707',
    fill=True,
    fill_color='#bc0d0d'
).add_to(m),
'''
# Generate Map
m.save('map.html')
