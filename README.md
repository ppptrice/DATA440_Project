# DATA440_Project
Automations and Workflows project

In this project, I'd like to simulate an aspect of the immune response in a body when presented with a stressor. This involves the simulation of cytokine and chemokine levels. The project will gather summary statistics from a cytokine dataset in order to determine the baseline cytokine levels in a healthy human adult body. The user may generate a random individual's cytokine data depending on the current data provided. The random individual will have cytokine levels dependent on the dataset's mean and variance of each cytokine level.
The user can select different cytokines to explore using the sidebar in streamlit.

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
  - use seaborn to make visualization nicer
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
- The streamlit webstie should pop up in your browser!
