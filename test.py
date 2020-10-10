import json
MAPBOX_API_KEY = json.load(open("tokens.json", "r"))["pub_tok"]
import pydeck as pdk
HEXAGON_LAYER_DATA = (
    "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"  # noqa
)
print HEXAGON_LAYER_DATA

# Define a layer to display on a map
layer = pdk.Layer(
    "HexagonLayer",
    HEXAGON_LAYER_DATA,
    get_position=["lng", "lat"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1,
)

# Set the viewport location
view_state = pdk.ViewState(
    longitude=-1.415, latitude=52.2323, zoom=6, min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36,
)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state, mapbox_key=MAPBOX_API_KEY)
r.to_html("hexagon_layer.html")
