import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation <= 2000:
        return 'red'
    elif elevation <= 3000:
        return 'purple'
    else:
        return 'blue'


map = folium.Map(
    location=[40.599608, -75.497870], zoom_start=5, tiles="Mapbox Bright")

fg_vol = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fg_vol.add_child(
        folium.CircleMarker(
            [lt, ln],
            radius=10,
            popup=str(el) + ' m ',
            color='black',
            fill=True,
            fill_color=color_producer(el),
            fill_opacity=0.8))

fg_pop = folium.FeatureGroup(name="Population")

fg_pop.add_child(
    folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_vol)
map.add_child(fg_pop)

map.add_child(folium.LayerControl())

map.save("Map1.html")
