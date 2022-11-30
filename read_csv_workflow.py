# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:10:24 2022

@author: sp2di
"""

# Import 
import pandas as pd

# Read 
data = pd.read_csv('vt_tax_data_2016.csv')

# View
print(data.head())

# Load TSV 
data = pd.read_csv('vt_tax_data_2016.tsv', sep = '\t')

# Plot total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
#plt.show()

# list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

# next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=list(vt_data_first500))

# Vermont dataframes
print(vt_data_first500.head())
print(vt_data_next500.head())

# Load 
data = pd.read_csv("vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)



# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub": "category",
			  "zipcode": str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

# Create dict specifying that 0s in zipcode are NA values
null_values = {"zipcode": 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])


try:
  # Import the CSV without any keyword arguments
  data = pd.read_csv('vt_tax_data_2016_corrupt.csv')
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
    
    
try:
  # Import CSV with error_bad_lines set to skip bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines = False)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines = True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")