import pandas as pd
import numpy as np
import config
import os
# from scipy.stats import ttest_ind, chi2_contingency
# from statsmodels.stats.weightstats import DescrStatsW


class DataLoader:

    def __init__(self, data_path, seed):
        self.data_path = data_path
        self.seed = seed
        self.df = None

    def load_data(self):
        
        if os.path.exists(self.data_path):
            self.df = pd.read_csv(self.data_path)

            return self.df
        
        else:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        

    def assignment_prep(self):
        df = self.load_data()
        sample_df = df.sample(frac=0.75, random_state=self.seed)  
        return sample_df
        


