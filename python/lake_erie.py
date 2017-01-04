import gmplot

gmap = gmplot.GoogleMapPlotter(42.2, -81, 9)

# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)


marker_lats = [43.0023, 42.6637, 43.2556, 42.9167, 44.2112]
marker_lngs = [-82.4197, -82.5076, -79.0559, -78.9001, -76.2375]




gmap.scatter(marker_lats, marker_lngs, 'r', marker=True)
# gmap.plot(marker_lats, marker_lngs, 'cornflowerblue', edge_width=10)
# gmap.scatter(marker_lats, marker_lngs, '#3B0B39', size=40, marker=False)
# gmap.heatmap(marker_lats, marker_lngs)


gmap.draw("mymap.html")
