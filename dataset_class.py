import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# class to test out data generation methods
class dataset:
    def __init__(self, 
                 data,
                 ):
        
        if type(data) != pd.DataFrame:
            self.__PATH_TO_DATA = 'data/' + data
            self.data = self.__load_data()
        else: 
            self.data = data
            
        self.data_summary = self.data.describe()
        
    def __load_data(self):
        # kind of janky since it only works for the specific dataset
        dat = pd.read_csv(self.__PATH_TO_DATA)
        dat = dat.set_index('Unnamed: 1')
        for col in dat.columns:
            #print(col)
            if 'Unnamed' in col:
                #print(col)
                dat = dat.drop(col, axis = 1)
        dat = dat.drop('Sample ID') 
        dat.index.name = 'Sample_ID'
        for col in dat.columns:
            dat[col] = dat[col].apply(float)
            
        return dat
        
    # Input a list of columns to get summary stats
    def get_summary(self, cols = None): 
        if cols == None:
            return self.data_summary
        elif cols != None:
            return self.data_summary[cols]
    
    def get_dataframe(self):
        return self.data
    
    def get_means(self, cols = None):
        return self.get_summary(cols).iloc[1]
    
    def get_variance(self, cols = None):
        return self.get_summary(cols).iloc[2]
    
    def generate_hist(self, 
                      col = None, 
                      n_records = 126, 
                      compare_dists = True,
                      distribution = 'poisson',
                      prob = 0.5
                      ):
        '''
        Simulates a histogram of levels of a specific cytokine based on the original data. 
        There are options to compare the simulated histogram to the original data.
        distribution = ['poisson', 'normal']
        '''
        if distribution == 'poisson':
            x = np.random.poisson(lam = self.get_means(cols = col), size = n_records)
        elif distribution == 'normal':
            x = np.random.normal(loc = self.get_means(cols = col), scale = self.get_variance(cols = col), size = n_records)
        elif distribution == 'negative binomial':
            x = np.random.negative_binomial(n=self.get_means(cols = col), p = prob, size = n_records)
            
        if compare_dists == False:
            fig = plt.figure(figsize=(8,4))
            plt.hist(x=x)
            plt.title(col + ': Randomly generated distribution')
            #plt.show()
            return fig
        else:
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
        return f
    
    def generate_records(self, 
                         cols,
                         n_records = 1,
                         distribution = 'poisson',
                         prob = 0.5
                         ):
        df = pd.DataFrame()
        if distribution == 'poisson':
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