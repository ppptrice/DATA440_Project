import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from dataset_class import dataset

# Header of the website
st.write("""
# Simple simulation of normal human cytokine levels
The following tools help to coceptualize, visualize, and explore different cytokines of the immune system.
First, what is a cytokine?

A cytokine is a broad classifier for different groups of small proteins that are secreted 
to impact another cell. They are important in several different areas:
- cell signalling
- immune system functions
- physiological processes
""")

# Description of entire dataframe
st.write("""
Below is a section of a dataframe containing many different cytokine levels of normal, healthy humans. 
The data are measured in mean fluorescence intensity (MFI).
""")

# Creation of a "dataset" class that allows specific functions to be called later
cyto_dataset = dataset('norm_cytokine_data.csv')
df = cyto_dataset.get_dataframe()
st.write(df.head()) # inserts dataframe with all data

st.sidebar.header('Cytokine selection') # creates sidebar with title

# Creating selection of cytokines using sidebar
unique_cyto = df.columns.values
selected_cyto = st.sidebar.multiselect('Cytokines used in', unique_cyto, unique_cyto)
df_selected_cyto = df[selected_cyto]

# 
st.header('Dataframe of selected cytokines')
st.write("""The following dataframe displays all cytokines that are selected on the sidebar to the left, 
under 'Cytokine selection'.
""")
st.write('Current cytokines: ' + str([cyto for cyto in selected_cyto]))
st.write('Data Dimension: ' + str(df_selected_cyto.shape[0]) + ' rows and ' + str(df_selected_cyto.shape[1]) + ' columns.')
st.dataframe(df_selected_cyto)

# Summary statistics dataframe generation
st.header('Summary statistics of selected cytokines')
st.dataframe(cyto_dataset.get_summary(cols = selected_cyto))

# Displays a histogram of cytokine data generated depending on the selected distribution in the sidebar
st.header('Simulated histogram')
cyto_option = st.sidebar.selectbox('Histogram cytokine:', unique_cyto)
'Selected cytokine: ', cyto_option

dist_option = st.sidebar.selectbox('Type of distribution:', ['poisson', 'normal'])
'Selected distribution: ', dist_option

hist_fig = cyto_dataset.generate_hist(col = cyto_option, distribution = dist_option)

st.pyplot(hist_fig)

if st.button('Correlation Heatmap'):
    st.header('Correlation Heatmap')
    df_selected_cyto.to_csv('output.csv',index=False)
    corr_df = pd.read_csv('output.csv')

    corr = corr_df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots()
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)
    
st.sidebar.header('Cytokine selection for data generation')
    
generate_cyto = st.sidebar.multiselect('Cytokines to generate', unique_cyto, unique_cyto)
dist_option2 = st.sidebar.selectbox('Type of distribution to generate:', ['poisson', 'normal'])
num_records = st.sidebar.slider('Number of records to generate', 1, 500, 250)


st.header('Cytokine dataframe generation')
'Selected distribution: ', dist_option2
#'Cytokines generated', generate_cyto
st.dataframe(cyto_dataset.generate_records(cols = generate_cyto, distribution = dist_option2, n_records = num_records))

def streamlit_defaults():
    '''
    Remove some auto-generated stuff by streamlit
    '''
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    return

streamlit_defaults()