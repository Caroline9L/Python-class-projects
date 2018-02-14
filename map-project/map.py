import folium
import pandas

#read from a txt file:
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

#to dynamically change marker colors:
def color_producer(elevation):
    if elevation <= 2000:
        return 'red'
    elif elevation <= 3000:
        return 'purple'
    else:
        return 'blue'

#basic map with 1 marker
# map = folium.Map(location=[40.599608, -75.497870])
#  map.add_child(folium.Marker(location=[40.599608, -75.497870], popup="I can see my house from here!", icon=folium.Icon(color='green')))

#map with zoom + tile
map = folium.Map(location=[40.599608, -75.497870], zoom_start=5, tiles="Mapbox Bright")

#feature group
# fg = folium.FeatureGroup(name="my map")

fg_vol = folium.FeatureGroup(name="Volcanoes")

#add single marker
# fg.add_child(
#     folium.Marker(
#         location=[40.599608, -75.497870],
#         popup="I can see my house from here!",
#         icon=folium.Icon(color='green')))

#add multiple markers
# for coordinates in [[40.599608, -75.497870], [36.120445, -115.167458]]:
# 	fg.add_child(folium.Marker(location=coordinates, popup="I can see my house from here!", icon=folium.Icon(color='green')))

#read from a txt file:
# for lt, ln, el in zip(lat, lon, elev):
#     fg.add_child(
#         folium.Marker(
#             location=[lt, ln],
#             # popup=folium.Popup(str(el) + ' m ' + str(nm), parse_html=True), #if var has quotes in it
#             popup=str(el) + ' m ',
#             # icon=folium.Icon(color='green')))
#    icon=folium.Icon(color=color_producer(el))))

for lt, ln, el in zip(lat, lon, elev):
    fg_vol.add_child(
        folium.CircleMarker( #Marker
            [lt, ln],
            radius=10,
            popup=str(el) + ' m ',
            # icon=folium.Icon(color='green')))
            color='black',
            fill=True,
            fill_color=color_producer(el),
            fill_opacity=0.8))

# layer to read a json file and style the layer according to information with a lambda fn
fg_pop = folium.FeatureGroup(name="Population")

fg_pop.add_child(
    folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_vol)
map.add_child(fg_pop)

# layer control layer to turn layers on and off on the map itself. Goes AFTER the fg declaration (map.add_child(fg) - the command to add all those fgs above) so that it executes at the end
map.add_child(folium.LayerControl()) #if fg are not specified as separate, all will be treated as one layer

map.save("Map1.html")
