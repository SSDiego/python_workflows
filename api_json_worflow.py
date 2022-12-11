# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 01:43:06 2022

@author: sp2di
"""

### Lendo Json 1

import pandas as pd
pop_in_shelters = pd.read_json('dhs_daily_report.json')
print(pop_in_shelters.describe())


try:
    # Especificando a orientação
    df = pd.read_json("dhs_report_reformatted.json",
                      orient = 'split')
    
    # Plot de população em abrigos ao longo do tempo
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("Erro com JSON parse.")
    
    
### Interagindo com APIs  2   

api_url = "https://api.yelp.com/v3/businesses/search"

### Usando get para pegar os dados
response = requests.get(api_url, 
                headers=headers, 
                params=params)

### Em response utiliza-se o método json() para salvar os dados em 'data'
data = response.json()

### Criando o DF
cafes = pd.DataFrame(data['businesses'])

### View the data's dtypes
print(cafes.dtypes)

### Parâmetros 3

### Definindo parâmetro usando uma estrutura de dicionário
parameters = {"term": "cafe",
          	  "location": "NYC"}

### Construindo a query
response = requests.get(api_url, 
                        headers=headers, 
                        params=parameters)

### Extraindo com o método json()
data = response.json()

### Criando o DF
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())


### 4

### Autorização e chave de acesso definidos pelo site
headers = {"Authorization": "Bearer {}".format(api_key)}

# QQuery
response = requests.get(api_url, 
                        headers=headers, 
                        params=params)

# Extração com .json()
data = response.json()

# DF
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)




#5 

# Chamar json_normalize()
from pandas.io.json import json_normalize

# Extrair com json()
data = response.json()

# Estruturando os dados
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())


#6

# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                            sep="_")

# View the data
print(flat_cafes.head())


#7 

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())


#8

# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories")

# View the data
print(flat_cafes.head())


#9

# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates", "latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())



#10

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, 
                   			   left_on="location_zip_code", 
                               right_on="zipcode")

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on="puma")

# View the data
print(cafes_with_pop.head())

