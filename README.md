# DATA440_Project
Automations and Workflows project

In this project, I take a look at a specific aspect of the human body that regulates immune system functions, cytokines. Cytokines act as signalling molecules to modulate key components of the immune system, like helper T cells, macrophage recruitment, B cells, and numerous other cells/processes. Cytokines are measured here in mean fluorescence intensity (MFI), with a higher number indicating higher cytokine levels. The project will explore a cytokine dataset to display the relationships between different cytokines, as well as to explore different distributions modelling normal, healthy human cytokine levels. The user may generate a random individual's cytokine data depending on the current data provided and have access to a couple different visualization options. The random individual will have cytokine levels dependent on the dataset's mean and variance of each cytokine level.

The project is meant to be more exploratory than explanatory, although there are still some fun results to find within the data!

Current objectives
---
- write functions to visualize summary statistics of the data depending on user input
  - histogram function that randomly generates data using a specified distribution
- generate random data with a function based on the cytokine data
  - model the distribution of the data (normal, poisson, etc.)
- create an interactive streamlit site allowing exploration of the data

Streamlit objectives
---
Integrate interactivity via user input:
- sidebar menu with cytokine selection for viewing in dataframe
- option to generate histograms showing different distributions
- show relationships between different cytokines

Streamlit functionality
---
The current streamlit site hosts a few tools to look at the data. 
The site provides a bit of information on cytokines, some dataframes to view and generate data, 
and a couple of visualizations to show the general shape of the data.

### Introduction + cytokine dataframe
Starting from the top of the page, the introduction provides brief information on cytokines. 
The data from the norm_cytokine_data.csv are displayed as a dataframe. The sample ID is from the cytokine data,
but I decided not to remove it. Each column contains the MFI for one individual healthy human blood sample.

### Selected cytokine dataframe
This section has a dataframe that updates based on the sidebar selection on the left. The sidebar allows
users to change the contents of the page based on the inputs. In this section, the sidebar menu titled
'Cytokines used in data selection' changes which cytokines are displayed in the dataframe.

### Cytokine summary statistics
Next on the page is summary statistics calculated used the .describe() function from pandas. 
This includes the mean, median, standard deviation, etc.
Each cytokine has 126 observations, indicating 126 different people from which the data are collected.
This dataframe adjusts to the cytokines that have been selected on the sidebar on the left of the page. 
Users may select certain cytokines to be displayed in this summary dataframe. Additionally, the text under this section
will be updated with the selection in the sidebar.

### Simulated histograms
In this section, two histograms will be shown depending on the cytokine and distribution selected on the sidebar to the left. 
The left histogram shows the cytokine levels for the normal cytokine data, while the right histogram uses randomly generated data
depending on the selected distribution on the sidebar under 'Cytokine selection'. The user can play around with different cytokines and 
distributions to find one that best models the normal levels of the selected cytokine. The text in this section also updates so that
the user may collapse the sidebar and still see the current distribution and cytokine.

### Correlation heatmap
This section shows a heatmap of the selected cytokines on the sidebar under 'Cytokine selection'. The heatmap displays
the strength of the correlation between selected cytokines, allowing users to see at a glance which cytokines are related.
There is also the option to display the correlation coefficient on the graph. As shown, deeper red hues mean there is a stronger correlation
between the two cytokines. 

### Cytokine dataframe generation
The last section allows for generation of a downloadable dataframe using specified cytokines and distribution on the sidebar under 
'Cytokine selection for data generation'. The cytokines data generated here correspond to the 'Cytokines to generate' section, which is the second 
multiselect dropdown. It has similar parameters to the previous histogram, but there is now the option to change how many 
records/rows are in the dataframe. 

### Notes on the sidebar
The sidebar to the left controls the content of the page. The first section 'Cytokine selection' is for use through the selected cytokines dataframe to 
the correlation heatmap. It has three parameters:
- A multiselect option for cytokine selection
- A single selection for the cytokine to be displayed in the histogram
- A single selection for the type of distribution in the histogram

The second section 'Cytokine selection for data generation' has parameters pertaining to the 'Cytokine Dataframe Generation' section at the bottom.
It also has three paramters:
- Multiselect for cytokines
- Slider to change number of rows in the dataframe
- Single selection for type of distribution

Please note that selecting 'negative binomial' will have a 'probability' popup where the user can adjust the probability used
in the data generation process for negative binomial distributions!




Additional notes
---

Data are sourced from:
- https://duke-hhis.github.io/reference-range/#/

To run the streamlit website:
1. Clone the repository
2. Navigate to the DATA440_Project folder in command prompt (powershell, terminal, etc.)
3. Run:
> pipenv shell

> pipenv install --ignore-pipfile

> streamlit run st_app.py

The streamlit website should pop up in your browser!
