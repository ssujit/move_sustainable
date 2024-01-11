import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import leafmap.foliumap as leaf
import os
os.chdir(r'/Users/sukantodas/Documents/work/ioer/files/pubdis')

st.set_page_config(page_title='Dashboard', page_icon=":de:", layout='wide')

st.title('Mobility Explorer')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

#st.sidebar.title('About')
#st.title('About')
#st.sidebar.info('Explore the summary stat of disparity')
st.info('Explore the summary stat of disparity')

st.header("Compare between morning and afternoon")
col1, col2 = st.columns((2))

@st.cache_data
def read_gdf(geo):
    gdf = gpd.read_file(geo)
    return gdf

@st.cache_data
def read_csv(summ):
    df = pd.read_csv(summ)
    return df

satam_gdf = read_gdf("satamo_hdn.gpkg")
satpm_gdf = read_gdf("satpmo_hdn.gpkg")
sunam_gdf = read_gdf("sunamo_hdn.gpkg")
sunpm_gdf = read_gdf("sunpmo_hdn.gpkg")
wkam_gdf = read_gdf("wkamo_hdn.gpkg")
wkpm_gdf = read_gdf("wkpmo_hdn.gpkg")
ct_gdf = read_gdf("city.gpkg")
stat_df = read_csv("hilden_stat.csv")
morning_df = read_csv("morning_time.csv")
noon_df = read_csv("noon_time.csv")

# Create the chart
cities = ct_gdf.city.values
city = st.sidebar.selectbox('Select a city', cities)
overlay = st.sidebar.checkbox('Overlay city')
city_stat = stat_df[stat_df['city'] == city]

fig, ax = plt.subplots(1, 1)
stat_df.plot(kind='bar', ax=ax, color=['blue', 'red', 'green'],
    ylabel='pti', xlabel='stattistics')
ax.get_xaxis().set_ticklabels([])
stats = st.sidebar.pyplot(fig)

with col1:
    morning = morning_df.time.values
    time = st.selectbox('Morning', morning)
with col2:
    noon = noon_df.time.values
    time = st.selectbox('Afternoon', noon)
    

with col1:
    # First Map
    st.subheader('During Morning')
    m1 = leaf.Map(
        layers_control=True,
        draw_control=False,
        measure_control=False,
        fullscreen_control=False,
    )
    m1.add_basemap('CartoDB.DarkMatter')
    # adding wk_am layer
    m1.add_gdf(
        gdf= wkam_gdf,
        zoom_to_layer=False,
        layer_name='wk_am',
        info_mode='on_click',
        style={'color': '#7fcdbb', 'fillOpacity': 0.3, 'weight': 0.8},
    )
    # adding sat_am layer
    m1.add_gdf(
        gdf= satam_gdf,
        zoom_to_layer=False,
        layer_name='sat_am',
        info_mode='on_click',
        style={'color': '#759242', 'fillOpacity': 0.3, 'weight': 0.8},
    )
    # adding sun_am layer
    m1.add_gdf(
        gdf= sunam_gdf,
        zoom_to_layer=False,
        layer_name='sun_am',
        info_mode='on_click',
        style={'color': '#A59CD3', 'fillOpacity': 0.3, 'weight': 0.8},
    )

    if overlay:
        m1.add_gdf(
            gdf=ct_gdf,
            zoom_to_layer=False,
            layer_name='cities',
            info_mode=None,
            style={'color': '#225ea8', 'weight': 1.5},
        )

    selected_gdf = ct_gdf[ct_gdf['city'] == city]

    m1.add_gdf(
        gdf=selected_gdf,
        layer_name='selected',
        zoom_to_layer=True,
        info_mode=None,
        style={'color': 'yellow', 'fill': None, 'weight': 2}
     )
    m1_streamlit = m1.to_streamlit(480, 500)

with col2:
    # Second Map
    st.subheader('During Aternoon')
    m2 = leaf.Map(
        layers_control=True,
        draw_control=False,
        measure_control=False,
        fullscreen_control=False,
    )
    m2.add_basemap('CartoDB.DarkMatter')
    # adding wk_pm layer
    m2.add_gdf(
        gdf= wkpm_gdf,
        zoom_to_layer=False,
        layer_name='wk_pm',
        info_mode='on_click',
        style={'color': '#7fcdbb', 'fillOpacity': 0.3, 'weight': 0.8},
    )
    # adding sat_pm layer
    m2.add_gdf(
        gdf= satpm_gdf,
        zoom_to_layer=False,
        layer_name='sat_pm',
        info_mode='on_click',
        style={'color': '#759242', 'fillOpacity': 0.3, 'weight': 0.8},
    )
    # adding sun_pm layer
    m2.add_gdf(
        gdf= sunpm_gdf,
        zoom_to_layer=False,
        layer_name='sun_pm',
        info_mode='on_click',
        style={'color': '#A59CD3', 'fillOpacity': 0.3, 'weight': 0.8},
    )

    if overlay:
        m2.add_gdf(
            gdf=ct_gdf,
            zoom_to_layer=False,
            layer_name='cities',
            info_mode=None,
            style={'color': '#225ea8', 'weight': 1.5},
        )

    selected_gdf = ct_gdf[ct_gdf['city'] == city]

    m2.add_gdf(
        gdf=selected_gdf,
        layer_name='selected',
        zoom_to_layer=True,
        info_mode=None,
        style={'color': 'yellow', 'fill': None, 'weight': 2}
     )
    m2_streamlit = m2.to_streamlit(480, 500)
    
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