import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from dataset_class import dataset

# Header of the website
st.write("""
# Simple Simulation of Normal Human Cytokine Levels 
---
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

############ ENTIRE DATASET
# Creation of a "dataset" class that allows specific functions to be called later
cyto_dataset = dataset('norm_cytokine_data.csv')
df = cyto_dataset.get_dataframe()
st.write(df.head()) # inserts dataframe with all data

st.sidebar.header('Cytokine selection') # creates sidebar with title

# Creating selection of cytokines using sidebar
unique_cyto = df.columns.values
selected_cyto = st.sidebar.multiselect('Cytokines used in data selection', unique_cyto, unique_cyto)
df_selected_cyto = df[selected_cyto]


################# SELECTED CYTOKINE DATAFRAME
# 
st.header('Dataframe of Selected Cytokines')
st.divider()
st.write("""The following dataframe displays all cytokines that are selected on the sidebar to the left, 
under 'Cytokine selection'.
""")
st.write('Current cytokines: ' + str([cyto for cyto in selected_cyto]))
st.write('Data Dimension: ' + str(df_selected_cyto.shape[0]) + ' rows and ' + str(df_selected_cyto.shape[1]) + ' columns.')
st.dataframe(df_selected_cyto)


############## SUMMARY STATISTICS
# Summary statistics dataframe generation
st.header('Summary Statistics of Selected Cytokines')
st.divider()
st.write('''The following dataframe displays simple summary statistics of the data.
They will also adjust to the selected cytokines on the sidebar under 'Cytokine selection'
''')
st.dataframe(cyto_dataset.get_summary(cols = selected_cyto))


############## HISTOGRAM
# Displays a histogram of cytokine data generated depending on the selected distribution in the sidebar
st.header('Simulated Histogram')
st.divider()
st.write('''This visualization allows you to test out several different distributions to model 
the specified cytokine selected on the sidebar.
''')
cyto_option = st.sidebar.selectbox('Histogram cytokine:', unique_cyto)
'Selected cytokine: ', cyto_option

dist_option = st.sidebar.selectbox('Type of distribution:', ['poisson', 'normal', 'negative binomial'])
'Selected distribution: ', dist_option

if dist_option == 'negative binomial':
    nbinom_prob = st.sidebar.number_input(label = 'Insert the probability for the negative binomial distribution',
                                          min_value = 0.000001, max_value = 1.0, value = 0.5, step = 0.01)
    hist_fig = cyto_dataset.generate_hist(col = cyto_option, distribution = dist_option, prob = nbinom_prob)
else:
    hist_fig = cyto_dataset.generate_hist(col = cyto_option, distribution = dist_option)

st.pyplot(hist_fig)


############ CORRELATION HEATMAP
#if st.button('Correlation Heatmap'):
st.header('''Correlation Heatmap
---''')
st.write("""This heatmap shows any possible correlations between the selected cytokines on the sidebar.
It may be useful to discern relationships between certain cytokines (e.g. pro-inflammatory cytokines may
be correlated with each other).
""")
df_selected_cyto.to_csv('output.csv',index=False)
corr_df = pd.read_csv('output.csv')

corr_nums = st.checkbox(label = 'Display correlation numbers on heatmap?')

corr = corr_df.corr()
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots()
    ax = sns.heatmap(corr, mask=mask, vmax=1, vmin=-1, square=True,
                     annot=corr_nums, fmt=".2f", linewidth = .5, cmap='vlag',
                     annot_kws={"size": 30 / np.sqrt(len(corr))})
st.pyplot(f)


############### GENERATED CYTOKINE DATA
st.sidebar.header('Cytokine selection for data generation')
    
generate_cyto = st.sidebar.multiselect('Cytokines to generate', unique_cyto, unique_cyto)
dist_option2 = st.sidebar.selectbox('Type of distribution to generate:', ['poisson', 'normal', 'negative binomial'])
num_records = st.sidebar.slider('Number of records to generate', 1, 500, 250)

st.header('Cytokine Dataframe Generation')
st.divider()
'Selected distribution: ', dist_option2
st.write('''Using the sidebar, you can generate your own data using the specified parameters!
Below is the dataframe you created.
''')
#'Cytokines generated', generate_cyto
if dist_option2 == 'negative binomial':
    nbinom_prob2 = st.sidebar.number_input(label = 'Input the probability for the negative binomial distribution',
                                          min_value = 0.000001, max_value = 1.0, value = 0.5, step = 0.01)
    st.dataframe(cyto_dataset.generate_records(cols = generate_cyto, distribution = dist_option2, n_records = num_records, prob = nbinom_prob2))
else:
    st.dataframe(cyto_dataset.generate_records(cols = generate_cyto, distribution = dist_option2, n_records = num_records))


################ removes the bottom text
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