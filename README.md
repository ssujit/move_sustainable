# About 
This repository hosts the code and resources for public transit visualization, a streamlit cloud-based dashboard designed to explore the mobility in public transit service frequency using GTFS data of Germany. It includes the graphical model builder tool of QGIS for processing raw GTFS data, generating Distance Indicators, and implementing Local Moran's Index for spatial analysis using python.
# Data
## GTFS
 
Primary data for this study is the open public transit feed data (GTFS). The GTFS data was collectedfrom (https://gtfs.de/de/feeds). They offer 3 different types of data for Germany. These are: 1) Long Distance Rail 2) Local Transit and 3) Regional Rail. For the current study local transit and regional rail data were downloaded. This data comes in .zip format. GTFS data of Germany contains 8 text files in .txt format. Table 1 shows details information of each text file. Though, it was supposed to be updated every week, author noticed during the study period same data was provided until 10.08.2022.

### Table 1: Properties of the Collected GTFS Data

|**Feed Name** | **File size (MB)**| **Unique trips** | **Stops** | **Date** |
|:---:| :---:|:---:|:---:|:---:| 
| Local transit Germany |181|1,3 M|460 K| July 10, 2022|
| Regional trains Germany|6,7|64 K|15 K| July 10, 2022|

## Structure of the Collected GTFS Data
It is seen from Table 2 that each of the collected GTFS dataset has 7 .txt files, apart from them GTFS data also have feed_info.txt file. Details of each file are given below:
### Table 2: Structure of the GTFS Files
|**File** | **Field 1**| **Field 2** | **Field 3** | **Field 4** |**Field 5**| **Field 6** | **Field 7** | **Field 8** | **Field 9** | **Field 10** |
|:---:| :---:|:---:|:---:|:---:|:---:| :---:|:---:|:---:|:---:|:---:|
|agency.txt|agency_id|agency_name|agency_url|agency_timezone| | |  | |  | |


# Jupyternotebooks
## Notebooks 
- [Exploratory data analysis](https://github.com/ssujit/move_sustainable/blob/main/notebook/1_exploratory_data_analysis.ipynb)
- [Spatial statistics with contiguity weights](https://github.com/ssujit/move_sustainable/blob/main/notebook/2_spatial_statistics_contiguity.ipynb)
- [Spatial statistics with KNN weights](https://github.com/ssujit/move_sustainable/blob/main/notebook/2_spatial_statistics_neighborhood.ipynb)


## Note: The interactive notebook can be run using GESIS binderhub: https://notebooks.gesis.org/binder/

# Demo Dashboard
Explore: [https://move-sustainable.streamlit.app](https://move-sustainable.streamlit.app) 
