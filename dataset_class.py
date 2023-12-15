import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# class to test out data generation methods on a dataframe containing cytokine data
# generally just has functions to get information on the data, like mean, variance, shape of the data

class dataset:
    def __init__(self, 
                 data, #should come in the form of a csv
                 ):
        
        if type(data) != pd.DataFrame:           # this is if the data is in the 'data' folder
            self.__PATH_TO_DATA = 'data/' + data
            self.data = self.__load_data()
        else:                                    # if people just want to put in an already-cleaned dataframe, 
            self.data = data                     # just set data to the data that is input
            
        self.data_summary = self.data.describe() # computes summary statistics for the dataset
                                                 # this is also so we don't have to keep computing stats later
        
    def __load_data(self):                       # cleans the messy data, but is only specific for the data i provided
        # kind of janky since it only works for the specific dataset
        dat = pd.read_csv(self.__PATH_TO_DATA)
        dat = dat.set_index('Unnamed: 1')        # sets the index to 'Sample ID'
        for col in dat.columns:                  # this loop drops all the 'Unnamed' columns since the measures are harder to process/interpret
            #print(col)
            if 'Unnamed' in col:
                #print(col)
                dat = dat.drop(col, axis = 1)
        dat = dat.drop('Sample ID')              # removes the first row in the data frame which just has MFI labels
        dat.index.name = 'Sample_ID'             
        for col in dat.columns:
            dat[col] = dat[col].apply(float)     # makes all data floats
            
        return dat
        
    # Input a list of columns to get summary stats like mean, variance, median, etc.
    def get_summary(self, 
                    cols:list = None             # cols should be a list of strings
                    ):          
        
        '''
        Returns the typical descriptive statistics of the data such as mean, median, and variance of specified columns. 
        '''
        if cols == None:                         # returns all columns from the previously-calculated summary, if none are specified
            return self.data_summary
        elif cols != None:                       # returns specified columns
            return self.data_summary[cols]
    
    def get_dataframe(self):                     # returns raw dataframe
        '''
        Returns the dataframe
        '''
        return self.data
    
    def get_means(self, cols = None):            # returns MEANS of the summary for specified columns
        '''
        Returns the means of the columns specified.
        'cols' is a list of strings with the columns in the dataframe 
        '''
        return self.get_summary(cols).iloc[1]
    
    def get_variance(self, cols = None):         # returns VARIANCES of the summary for specified columns
        '''
        Returns the variance of the columns specified
        '''
        return self.get_summary(cols).iloc[2]
    
    def generate_hist(self,                      # this function generates the histogram for a defined distribution
                      col:list = None,                # only one column can be selected at a time
                      n_records:int = 126, 
                      compare_dists:bool = True,      # this parameter is true if you want to return only the new/modelled histogram,
                                                 # and not the distribution ofthe actual data
                      distribution:str = 'poisson',    # default dist. is poisson
                      prob:float = 0.5                 # this parameter is for the negative binomial distribution
                      ):                         # if 'binomial is not specified, it has no effect on the function
        '''
        Simulates a histogram of levels of a specific cytokine based on the original data. 
        There are options to compare the simulated histogram to the original data 
        using different distributions specified below. 
        distribution = ['poisson', 'normal', 'negative binomial']
        '''
        
        # runs through different distribution options
        if distribution == 'poisson':            # creates data using poisson dist. and the mean calculated from the data
            x = np.random.poisson(lam = self.get_means(cols = col), size = n_records) 
        elif distribution == 'normal':           # creates data using normal dist. and the mean/variance from the data
            x = np.random.normal(loc = self.get_means(cols = col), scale = self.get_variance(cols = col), size = n_records)
        elif distribution == 'negative binomial':# creates data using negative binomial dist. using the mean from the data, and the 'prob' parameter
            x = np.random.negative_binomial(n=self.get_means(cols = col), p = prob, size = n_records)
            
        if compare_dists == False:               # this is not used in the streamlit, but is here if you only want the randomly generated dist.
            fig = plt.figure(figsize=(8,4))
            plt.hist(x=x)
            plt.title(col + ': Randomly generated distribution')
            #plt.show()
            return fig
        else:                                    # this is the default case where we compare the hist with generated data vs. the original data
            f = plt.figure(figsize=(8,8))
            f,[data_hist, new_hist] = plt.subplots(1,2, sharex=True)
            data_hist.hist(x = self.data[col], linewidth = 1, color = 'skyblue', bins = 15,
                           ec = 'white')
            new_hist.hist(x = x, linewidth = 1, color = 'firebrick',
                          ec = 'white')
            
            data_hist.tick_params(pad = 10)
            new_hist.tick_params(pad = 10)
            
            [data_hist.spines[i].set_visible(False) for i in data_hist.spines]
            [new_hist.spines[i].set_visible(False) for i in new_hist.spines]
            
            data_hist.set_title('Observed data')
            new_hist.set_title('Generated data')
        return f                                 # I had to return f in order for the histogram to display in streamlit
    
    # returns a new dataframe with randomly generated values depending on the distribution selected
    # it has very similar paramters as generate_hist() 
    def generate_records(self,                 
                         cols,
                         n_records = 1,
                         distribution = 'poisson',
                         prob = 0.5
                         ):
        
        df = pd.DataFrame()
        if distribution == 'poisson':            # All values are rounded, but some won't have decimals anyway
            for col in cols:
                df[col] = np.round(np.random.poisson(lam = self.get_means(cols = col), size = n_records), decimals = 2)
        elif distribution == 'normal':
            for col in cols:
                df[col] = np.round(np.random.normal(loc = self.get_means(cols = col), 
                                                    scale = self.get_variance(cols = col), 
                                                    size = n_records), decimals = 2)
        elif distribution == 'negative binomial':
            for col in cols:
                df[col] = np.round(np.random.negative_binomial(n=self.get_means(cols = col), 
                                                               p = prob, size = n_records), 2)
        return df