# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 09:19:19 2022

@author: sp2di
"""

# https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls




# Chamar create_engine
from sqlalchemy import create_engine 

# Usar função importada para criar a engine do banco
engine = create_engine('sqlite:///census.sqlite')


# Print table names
print(engine.table_names())


#--------------------------------------------------------------------------


# Reflection e Metadata

# create_engine, MetaData, Table
from sqlalchemy import create_engine, Table, MetaData

# engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Criar objeto MetaData chamado: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload= True, autoload_with= engine)

# Print census table metadata
print(repr(census))


#--------------------------------------------------------------------------


#census.columns.keys()

from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Coluna
print(census.columns.keys())

# Coluna e Tipo
print(repr(census))



#--------------------------------------------------------------------------



# Enquanto na sessão anterior criamos uma reflexão do Banco
# Aqui começaremos a usar de fato

from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Criar Conexão
connection = engine.connect()

# Criação da Query
stmt = 'SELECT * FROM census'

# Execute and fetch 
results = connection.execute(stmt).fetchall()

# Print results
print(results)



#--------------------------------------------------------------------------



# Streamline workflow

# select

# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)



#--------------------------------------------------------------------------



# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
# print(first_row['state'])
print(first_row[0])
#print(results[0][0])

# Print the 'state' column of the first row by using its name
print(first_row.state)
