import json
import os
import pandas as pd
MAPBOX_API_KEY = json.load(open("tokens.json", "r"))["pub_tok"]
import pydeck as pdk
data = json.load(open("out.json", "r"))
df = pd.read_csv("out.csv", sep="\n", lineterminator="\n", delimiter=",")
df = df[:-1]
data = data[1:]
df.columns = ["lng", "lat", "val"]
print df
#Daten\Unfallorte2016_EPSG25832_CSV\csv\Unfallorte_2016_LinRef.csv
layer = pdk.Layer(
    'ScatterplotLayer',
    df,
    get_position=["lng", "lat", "val"],
    auto_highlight=True,
    pickable=True,
    get_radius=500,
    get_fill_color=[180, 0, 200, 140],
    #elevation_scale=50,
    #elevation_range=[0, 3000],
    #extruded=True,
    #coverage=1
    )

layer2 = pdk.Layer(
    'HexagonLayer',
    df,
    get_position=["lng","lat", "val"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
    )
view_state = pdk.ViewState(
    longitude=13.30511, latitude=52.49548, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state,
            mapbox_key=MAPBOX_API_KEY,
            tooltip={'html': '<b>Elevation Value:</b> {elevationValue}',
                     'style': {
                     'color': 'white'
                               }
                    }
            )
r.to_html("hexagon_layer.html")
