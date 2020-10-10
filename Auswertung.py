import json
import os
import pandas as pd
MAPBOX_API_KEY = json.load(open("tokens.json", "r"))["pub_tok"]
import pydeck as pdk
data = json.load(open("out.json", "r"))
df = pd.read_csv((os.path.join("Daten", "Unfallorte2016_EPSG25832_CSV", "csv", "Unfallorte_2016_LinRef.csv")), sep="\t", lineterminator="\r")

#Daten\Unfallorte2016_EPSG25832_CSV\csv\Unfallorte_2016_LinRef.csv
layer = pdk.Layer(
    'ScatterplotLayer',
    data,
    get_position=['lng', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1)
view_state = pdk.ViewState(
    longitude=13.30511, latitude=52.49548, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state, mapbox_key=MAPBOX_API_KEY)
r.to_html("hexagon_layer.html")
