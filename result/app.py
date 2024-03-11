import streamlit as st
import geopandas as gpd
import leafmap.foliumap as leaf
import plotly.graph_objects as go

# github data url
url = 'https://raw.github.com/ssujit/move_sustainable/main/data/'

# data read and load
pti_data = 'aoi.geojson'
ct_poly = 'city.geojson'

area = gpd.read_file(f'{url}{pti_data}')
ct_boundary = gpd.read_file(f'{url}{ct_poly}')

st.set_page_config(page_title='Mobility Explorer', page_icon=":globe_with_meridians:", layout='wide')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

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
    
    # time filter
    dt = area["Time"].unique()
    time = st.sidebar.selectbox('Day Time', sorted(dt))
    
    # week filter
    wk = area["Type"].unique()
    wk_time = st.sidebar.selectbox('Week type', sorted(wk))
    
    # city filter
    ct_options = sorted(area["City"].unique())
    city = st.sidebar.selectbox('Select city', ct_options)
    
    filtered_ct = ct_boundary[ct_boundary["city"].isin([city])]
    

    filtered_df = area[
        (area["Time"].isin([time])) &
        (area["Type"].isin([wk_time])) &
        (area["City"].isin([city]))
    ]
   
    # Initialize LeafMap instances
    m = leaf.Map(
        layers_control=True,
        draw_control=False,
        measure_control=False,
        fullscreen_control=False,
    )
    m.add_basemap('CartoDB.DarkMatter')
    # canvas layer
    m.add_gdf(
        gdf=filtered_df,
        zoom_to_layer=False,
        layer_name=str(wk_time) + '_' + str(time),
        info_mode='on_click',
        style={'color': '#7fcdbb', 'fillOpacity': 0.3, 'weight': 0.8},
    )
    selected_gdf = ct_boundary[ct_boundary["city"] == city]
    
    m.add_gdf(
        gdf=selected_gdf,
        layer_name=str(city),
        zoom_to_layer=True,
        info_mode=None,
        style={'color': 'yellow', 'fill': None, 'weight': 2}
    )
    m.to_streamlit(600, 400)

    
def page_compare():
    st.title('Comparison between city to city')
    st.header("Compare")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    st.sidebar.write("Write the relevant text about what this page is for")
    
    col1, col2 = st.columns((2))

    # time filter
    with col1:
        dt1 = area["Time"].unique()
        time1 = st.selectbox('Day Time 1', sorted(dt1))
    with col2:
        dt2 = area["Time"].unique()
        time2 = st.selectbox('Day Time 2', sorted(dt2))

    # week filter
    with col1:
        wk1 = area["Type"].unique()
        wk_time1 = st.selectbox('Week type 1', sorted(wk1))
    with col2:
        wk2 = area["Type"].unique()
        wk_time2 = st.selectbox('Week type 2', sorted(wk2))

    # city filter
    with col1:
        ct_options1 = sorted(area["City"].unique())
        city1 = st.selectbox('Select city 1', ct_options1)
    with col2:
        ct_options2 = sorted(area["City"].unique()) 
        city2 = st.selectbox('Select city 2', ct_options2)
        
    filtered_ct1 = ct_boundary[ct_boundary["city"].isin([city1])]
    filtered_ct2 = ct_boundary[ct_boundary["city"].isin([city2])]

    filtered_df1 = area[
        (area["Time"].isin([time1])) &
        (area["Type"].isin([wk_time1])) &
        (area["City"].isin([city1]))
    ]

    filtered_df2 = area[
        (area["Time"].isin([time2])) &
        (area["Type"].isin([wk_time2])) &
        (area["City"].isin([city2]))
    ]

    filtered_df1 = filtered_df1.dropna(subset=['fi'])
    filtered_df2 = filtered_df2.dropna(subset=['fi'])
    
    with col1:
        st.subheader('Canvas 1')
        # Initialize LeafMap instances
        m1 = leaf.Map(
            layers_control=True,
            draw_control=False,
            measure_control=False,
            fullscreen_control=False,
        )
        m1.add_basemap('CartoDB.DarkMatter')
        # canvas layer
        m1.add_data(
            filtered_df1,
            column="fi",
            scheme="Quantiles",
            k = 4,
            cmap="Blues",
            legend_title="Legend",
            zoom_to_layer=False,
            layer_name=str(wk_time1) + '_' + str(time1),
            info_mode='on_click',
        )
        selected_gdf1 = ct_boundary[ct_boundary["city"] == city1]
        
        m1.add_gdf(
            gdf=selected_gdf1,
            layer_name=str(city1),
            zoom_to_layer=True,
            info_mode=None,
            style={'color': 'yellow', 'fill': None, 'weight': 2}
        )
        m1.to_streamlit(450, 400)

    with col2:
        st.subheader('Canvas 2')
        m2 = leaf.Map(
            layers_control=True,
            draw_control=False,
            measure_control=False,
            fullscreen_control=False,
        )
        m2.add_basemap('CartoDB.DarkMatter')
        # adding wk_am layer
        m2.add_data(
            filtered_df2,
            column="fi",
            scheme="Quantiles",
            k = 4,
            cmap="Blues",
            legend_title="Legend",
            zoom_to_layer=False,
            layer_name=str(wk_time1) + '_' + str(time1),
            info_mode='on_click',
        )
        selected_gdf2 = ct_boundary[ct_boundary["city"] == city2]
        
        m2.add_gdf(
            gdf=selected_gdf2,
            layer_name=str(city2),
            zoom_to_layer=True,
            info_mode=None,
            style={'color': 'yellow', 'fill': None, 'weight': 2}
        )
        m2.to_streamlit(450, 400)
        
    with col1:
        st.subheader('Statistics of Canvas 1')
        fig1 = go.Figure()
        fig1.add_trace(go.Box(x=filtered_df1['fi'], boxmean=True))
        fig1.update_layout(xaxis_title='pti')
        fig1.update_layout(yaxis_title=str(wk_time1) + '_' + str(time1))
        st.plotly_chart(fig1)

    with col2:
        st.subheader('Statistics of Canvas 2')
        fig2 = go.Figure()
        fig2.add_trace(go.Box(x=filtered_df2['fi'], boxmean=True))
        fig2.update_layout(xaxis_title='pti')
        fig2.update_layout(yaxis_title=str(wk_time2) + '_' + str(time2))
        st.plotly_chart(fig2)
        
def main():
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
