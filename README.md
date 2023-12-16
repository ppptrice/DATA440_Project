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
- create boxplots,


Data are sourced from:
- https://duke-hhis.github.io/reference-range/#/

To run the streamlit website:
- Clone the repository
- Navigate to the DATA440_Project folder in command prompt (powershell, terminal, etc.)
- run:
> pipenv shell

> pipenv install --ignore-pipfile

> streamlit run st_app.py
- The streamlit website should pop up in your browser!
