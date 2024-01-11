import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import leafmap.foliumap as leaf
import os

os.chdir(r'/Users/sukantodas/Documents/work/ioer/files/pubdis')

#st.set_page_config(page_title='Dashboard', page_icon=":de:", layout='wide')

# Read data
sat_am = gpd.read_file("satamo_hdn.gpkg")
sat_pm = gpd.read_file("satpmo_hdn.gpkg")
sun_am = gpd.read_file("sunamo_hdn.gpkg")
sun_pm = gpd.read_file("sunpmo_hdn.gpkg")
wk_am = gpd.read_file("wkamo_hdn.gpkg")
wk_pm = gpd.read_file("wkpmo_hdn.gpkg")
ct_gdf = gpd.read_file("city.gpkg")
stat_df = pd.read_csv("hilden_stat.csv")
morning_df = pd.read_csv("morning_time.csv")
noon_df = pd.read_csv("noon_time.csv")

# Page functions
def page_about():
    st.title('Home')
    st.write("Welcome to Home Page!")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
    with st.expander("About"):
        st.write(
            """

             This is where we will describe the purpose of the dashboard
            """
        )
    st.sidebar.write("Write the relevant text about what this page is for")
    # Add more content for the home page as needed

def data_explorer():
    st.title('Data Explorer')
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
    st.sidebar.write("Write the relevant text about what this page is for")
    st.write("This is where you can learn more about the Mobility Explorer.")
    # Add more content for the about page as needed

def page_compare():
    st.title('Comparison')
    
    #st.set_page_config(page_title='Dashboard', page_icon=":de:", layout='wide')
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    st.header("Compare between morning and afternoon")
    st.sidebar.write("Write the relevant text about what this page is for")
    col1, col2 = st.columns((2))

    # ... (include relevant code from your original script)
    with col1:
        cities = ct_gdf.city.values
        city = st.sidebar.selectbox('Select city 1', cities)
        #overlay = st.sidebar.checkbox('Overlay city')
        city_stat = stat_df[stat_df['city'] == city]
    with col2:
        cities = ct_gdf.city.values
        city = st.sidebar.selectbox('Select city 2', cities)
        #overlay = st.sidebar.checkbox('Overlay city')
        city_stat = stat_df[stat_df['city'] == city]
        
    with col1:
        morning = morning_df.time.values
        time = st.selectbox('Morning', morning)
    with col2:
        noon = noon_df.time.values
        time = st.selectbox('Afternoon', noon)
    '''
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
            gdf= wk_am,
            zoom_to_layer=False,
            layer_name='wk_am',
            info_mode='on_click',
            style={'color': '#7fcdbb', 'fillOpacity': 0.3, 'weight': 0.8},
        )
        # adding sat_am layer
        m1.add_gdf(
            gdf= sat_am,
            zoom_to_layer=False,
            layer_name='sat_am',
            info_mode='on_click',
            style={'color': '#759242', 'fillOpacity': 0.3, 'weight': 0.8},
        )
        # adding sun_am layer
        m1.add_gdf(
            gdf= sun_am,
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

#selected_gdf = ct_gdf[ct_gdf['city'] == city]

        ##m1.add_gdf(
            #gdf=selected_gdf,
            #layer_name='selected',
            #zoom_to_layer=True,
            #info_mode=None,
            #style={'color': 'yellow', 'fill': None, 'weight': 2}
        # )
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

    # ... (include relevant code from your original script)

    with col1:
        pti_values = [df['pti'].dropna() for df in [wk_am, wk_pm, sat_am, sat_pm, sun_am, sun_pm]]
        plt.boxplot(pti_values, labels=['wk_am', 'wk_pm', 'sat_am', 'sat_pm', 'sun_am', 'sun_pm'], vert=False)
        plt.xlabel('pti Values')
        plt.ylabel('time')
        plt.title('Boxplot for all')
        plt.show()

    with col2:
        fig, ax = plt.subplots()
        stat_df.plot(kind='bar', ax=ax, color=['blue', 'red', 'green'],
            ylabel='pti', xlabel='stattistics')
        ax.get_xaxis().set_ticklabels([])
        stats = st.pyplot(fig)
'''
def main():
    st.set_page_config(page_title='Mobility Explorer', page_icon=":de:", layout='wide')

    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ("About", "Data Explorer", "Compare"))

    if page == "About":
        page_about()
    elif page == "Data Explorer":
        data_explorer()
    elif page == "Compare":
        page_compare()

if __name__ == "__main__":
    main()

