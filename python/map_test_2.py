import folium
map_osm = folium.Map(location=[59.402844, 10.796076], tiles='Stamen Terrain', zoom_start=13)
# map_osm.simple_marker(location=[59.402844, 10.796076], popup='1', marker_icon='info-sign')
# map_osm.simple_marker(location=[59.402844, 10.786056], popup='2', marker_icon='info-sign')
map_osm.save(outfile='osm.html')


