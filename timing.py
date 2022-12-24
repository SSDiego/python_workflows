# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:18:56 2022

@author: sp2di
"""


# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

%timeit nums_list_comp = [num for num in range(51)]


# Create a list of integers (0-50) by unpacking range
nums_unpack = [range(51)]
print(nums_unpack)

%timeit nums_unpack = [range(51)]


# Create a list using the formal name
%timeit formal_list = list()
print(formal_list)

# Create a list using the literal syntax
%timeit literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))



%%timeit
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)
    
%%timeit    
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462    


%load_ext line_profiler

%lprun -f convert_units convert_units(heroes, hts, wts)


def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)





import sys
from file import function

nums_list = [*range(1000)]
sys.getsizeof(nums_list)

%load_ext memory_profiler
%mprun -f convert_units convert_units(heroes, hts, wts)



def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis

%mprun -f convert_units convert_units(heroes, hts, wts)



def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes


def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes




# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))
