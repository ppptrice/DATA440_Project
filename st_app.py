import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from dataset_class import dataset


st.write("""
# Simple simulation of normal human cytokine levels
Below is a section of a dataframe containing many different cytokine levels of normal, healthy humans. 
The data are measured in mean fluorescence intensity (MFI).
""")

cyto_dataset = dataset('norm_cytokine_data.csv')
df = cyto_dataset.get_dataframe()

st.write(df.head())

st.sidebar.header('Cytokine selection')

unique_cyto = df.columns.values
selected_cyto = st.sidebar.multiselect('Cytokines', unique_cyto, unique_cyto)
df_selected_cyto = df[selected_cyto]

st.header('Dataframe of selected cytokines')
st.write('Data Dimension: ' + str(df_selected_cyto.shape[0]) + ' rows and ' + str(df_selected_cyto.shape[1]) + ' columns.')
st.dataframe(df_selected_cyto)

st.header('Summary statistics of selected cytokines')
st.dataframe(cyto_dataset.get_summary(cols = selected_cyto))

st.header('Simulated histogram')
cyto_option = st.sidebar.selectbox('Cytokine data to generate:', unique_cyto)
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