# About this 
this a repository for visualization of public transit in Germany
# Data
## GTFS
 
Primary data for this study is the open public transit feed data (GTFS). The GTFS data was collectedfrom (https://gtfs.de/de/feeds). They offer 3 different types of data for Germany. These are: 1) Long Distance Rail 2) Local Transit and 3) Regional Rail. For the current study local transit and regional rail data were downloaded. This data comes in .zip format. GTFS data of Germany contains 8 text files in .txt format. Table 1 shows details information of each text file. Though, it was supposed to be updated every week, author noticed during the study period same data was provided until 10.08.2022.

# Jupyternotebooks
## Notebooks 
- [Exploratory data analysis](https://github.com/ssujit/move_sustainable/blob/main/notebook/1_exploratory_data_analysis.ipynb)
- [Spatial statistics with contiguity weights](https://github.com/ssujit/move_sustainable/blob/main/notebook/2_spatial_statistics_contiguity.ipynb)
- [Spatial statistics with KNN weights](https://github.com/ssujit/move_sustainable/blob/main/notebook/2_spatial_statistics_neighborhood.ipynb)


## Note: The interactive notebook can be run using GESIS binderhub: https://notebooks.gesis.org/binder/

# Demo Dashboard
Explore: [https://move-sustainable.streamlit.app](https://move-sustainable.streamlit.app) 
