#!/usr/bin/env python3

import pandas as pd 
import numpy as np

class Handler():
    def __init__(self, df):
        self.df = df
    
    def data_overview(self):
        print(f"Number of rows: {len(self.df)}")
        print(f"Number of columns: {len(self.df.columns)}")
        print("\nData Types:")
        print(self.df.dtypes)
        print("\nDescriptive Statistics:")
        print(self.df.describe())
    
    def check_duplicate(self):
        # Identify and report duplicated values
        duplicates = self.df.duplicated()
        print("\nDuplicated values:")
        print(duplicates.sum(), "duplicated rows") 
    
    def calculate_missing_percentage(self):
        # Calculate and return the percentage of missing values in each column
        self.df.replace({'None':np.nan}, inplace=True)
        
        missing_values = self.df.isnull().sum()
        total_rows = len(self.df)
        
        # Correctly calculate the percentage for each column
        missing_values_percentage = (missing_values / total_rows) * 100
        
        # Convert the percentages to string format with 2 decimal places
        missing_values_percentage_str = missing_values_percentage.apply(lambda x: f'{x:.2f}%')
        
        # Concatenate the original missing values counts with their corresponding percentages
        new_df = pd.DataFrame({'Missing Values': missing_values, 'Percentage Missing': missing_values_percentage_str})
        
        print(new_df)
    
    def drop_columns(self):
        """Drop columns that contain missing values greater than 60% of the total."""
        # Calculate the percentage of missing values in each column
        missing_values_percentage = self.df.isnull().mean() * 100
        
        # Identify columns where the percentage of missing values is greater than 60%
        cols_to_drop = missing_values_percentage[missing_values_percentage > 60].index
        
        # Drop the identified columns
        self.df.drop(cols_to_drop, axis=1, inplace=True)
    
    def drop_missing_values(self):
        """drop missing values"""
        self.df.dropna(inplace=True)
    
    def remove_iqr_outliers(self):
        """
        Removes outliers from a DataFrame based on the Interquartile Range (IQR).
        """
        # Filter out non-numeric columns
        numeric_cols = self.df.select_dtypes(include=['float64']).columns
        
        # Apply the IQR method to numeric columns
        for col in numeric_cols:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            self.df.loc[self.df[col] < lower_bound, col] = lower_bound
            self.df.loc[self.df[col] > upper_bound, col] = upper_bound
        
        return self.df


