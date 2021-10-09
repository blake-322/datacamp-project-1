"""
Task 1: Instructions
Use our friend's data to create a dictionary. To do so, you will need to perform the following steps.

Create a list of years from 2011 to 2020 and a list durations of the average movie lengths our friend provided (103, 101, 99, 100, 100, 95, 95, 96, 93, and 90).
Create a dictionary movie_dict, with the keys "years" and "durations" and the values set to your lists years and durations.
Print and inspect the dictionary to ensure it was created correctly.
"""

#Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

#Create a dictionary with the two lists
moive_dict = {'years': years, 'durations': durations}

#Print the dictionary
print(movie_dict)
