import geopandas as gpd
import matplotlib.pyplot as plt



def bonus(file="data/map.geojson"):
    map = gpd.read_file(file)
    map.plot(figsize=(10, 8))
    plt.show()
