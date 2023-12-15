import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import leafmap.foliumap as leaf

url = 'https://raw.github.com/ssujit/mobility_explorer/main/data/'

wkam = 'wkamo_hdn.gpkg'
wkpm = 'wkpmo_hdn.gpkg'
satam = 'satamo_hdn.gpkg'
satpm = 'satpmo_hdn.gpkg'
sunam = 'sunamo_hdn.gpkg'
sunpm = 'sunamo_hdn.gpkg'
cen = 'ct_centroids.gpkg'
stat = 'hilden_stat.csv'
morning = 'morning_time.csv'
noon = 'noon_time.csv'

wk_am = gpd.read_file(f'{url}{wkam}')
wk_pm = gpd.read_file(f'{url}{wkpm}')
sat_am = gpd.read_file(f'{url}{satam}')
sat_pm = gpd.read_file(f'{url}{satpm}')
sun_am = gpd.read_file(f'{url}{sunam}')
sun_pm = gpd.read_file(f'{url}{sunpm}')
ct_cen = gpd.read_file(f'{url}{cen}')
stat_df = pd.read_csv(f'{url}{stat}')
morning_df = pd.read_csv(f'{url}{morning}')
noon_df = pd.read_csv(f'{url}{noon}')

st.set_page_config(page_title='Dashboard', page_icon=":de:", layout='wide')
st.title('Comparison')
    
#st.set_page_config(page_title='Dashboard', page_icon=":de:", layout='wide')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

st.header("Compare between morning and afternoon")
st.sidebar.write("Write the relevant text about what this page is for")

col1, col2 = st.columns((2))

with col1:
    morning = morning_df.time.values
    time = st.selectbox('Morning', morning)
with col2:
    noon = noon_df.time.values
    time = st.selectbox('Afternoon', noon)

with col1:
    cities = ct_cen.city.values
    city = st.selectbox('Select city 1', cities)
    city_1 = st.sidebar.checkbox(f'check {city} city', key=f'city_1_{city}')
    city_stat = stat_df[stat_df['city'] == city]
with col2:
    cities = ct_cen.city.values
    city = st.selectbox('Select city 2', cities)
    city_2 = st.sidebar.checkbox(f'check {city} city', key=f'city_2_{city}')

with col1:
    st.subheader('During Morning')
    m1 = leaf.Map(
        layers_control = True,
        draw_control = False,
        measure_control = False,
        fullscreen_control = False,
    )
    m1.add_basemap('CartoDB.DarkMatter')
    # adding wk_am layer
    m1.add_gdf(
        gdf = wk_am,
        zoom_to_layer=False,
        layer_name='wk_am',
        info_mode='on_click',
        style={'color': '#7fcdbb', 'fillOpacity': 0.3, 'weight': 0.8},
        )
    m1.add_gdf(
        gdf = sat_am,
        zoom_to_layer=False,
        layer_name='sat_am',
        info_mode='on_click',
        style={'color': '#759242', 'fillOpacity': 0.3, 'weight': 0.8},
        )
    m1.add_gdf(
        gdf = sun_am,
        zoom_to_layer=False,
        layer_name='sun_am',
        info_mode='on_click',
        style={'color': '#A59CD3', 'fillOpacity': 0.3, 'weight': 0.8},
        )
    
    if city_1:
        m1.add_gdf(
            gdf = ct_cen,
            zoom_to_layer = False,
            layer_name = cities,
            info_mode = None,
            style = {'color': '#225ea8', 'weight': 1.5},
            )
    selected_city = ct_cen[ct_cen['city'] == city]
    
    m1.add_gdf(
        gdf = selected_city,
        zoom_to_layer= False,
        layer_name = 'selected',
        info_mode = None,
        style = {'color': '#225ea8', 'weight': 1.5},
        )
    
    m1_streamlit = m1.to_streamlit(450, 400)

with col2:
    st.subheader('During Afternoon')
    m2 = leaf.Map(
        layers_control = True,
        draw_control = False,
        measure_control = False,
        fullscreen_control = False,
    )
    m2.add_basemap('CartoDB.DarkMatter')
    # adding wk_am layer
    m2.add_gdf(
        gdf = wk_pm,
        zoom_to_layer=False,
        layer_name='wk_pm',
        info_mode='on_click',
        style={'color': '#7fcdbb', 'fillOpacity': 0.3, 'weight': 0.8},
        )
    m2.add_gdf(
        gdf = sat_pm,
        zoom_to_layer=False,
        layer_name='sat_pm',
        info_mode='on_click',
        style={'color': '#759242', 'fillOpacity': 0.3, 'weight': 0.8},
        )
    m2.add_gdf(
        gdf = sun_pm,
        zoom_to_layer=False,
        layer_name='sun_pm',
        info_mode='on_click',
        style={'color': '#A59CD3', 'fillOpacity': 0.3, 'weight': 0.8},
        )
    
    if city_2:
        m2.add_gdf(
            gdf = ct_cen,
            zoom_to_layer = False,
            layer_name = cities,
            info_mode = None,
            style = {'color': '#225ea8', 'weight': 1.5},
            )
    selected_city = ct_cen[ct_cen['city'] == city]
    
    m2.add_gdf(
        gdf = selected_city,
        zoom_to_layer= False,
        layer_name = 'selected',
        info_mode = None,
        style = {'color': '#225ea8', 'weight': 1.5},
        )
    
    m2_streamlit = m1.to_streamlit(450, 400)

with col1:
    fig, ax = plt.subplots()
    stat_df.plot(kind='bar', ax=ax, color=['blue', 'red', 'green'],
        ylabel='pti', xlabel='stattistics')
    ax.get_xaxis().set_ticklabels([])
    stats = st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    stat_df.plot(kind='bar', ax=ax, color=['blue', 'red', 'green'],
        ylabel='pti', xlabel='stattistics')
    ax.get_xaxis().set_ticklabels([])
    stats = st.pyplot(fig)

    
