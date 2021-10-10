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

"""
Task 2: Instructions
    
Import pandas using its usual alias, pd.
Create a DataFrame durations_df using your movie_dict dictionary you created in the previous step.
Print the entire DataFrame.
"""

#Import pandas under its usual alias
import pandas as pd

#Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

#Print the DataFrame
print(durations_df)

"""
Task 3: Instructions

Import matplotlib.pyplot under the alias plt.
Create a line plot of the data with the years column of durations_df on the x-axis, and the durations column on the y-axis.
Add the title "Netflix Movie Durations 2011-2020" to your plot.
"""
#Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

#Draw a line plot of release_years and durations
plt.plot(durations_df['years'], durations_df['durations'])

#Create a title
plt.title('Netflix Movie Durations 2011-2020')

#Show the plot
plt.show()

"""
Task 4: Instructions

Create another DataFrame, netflix_df, this time using the CSV file our friend provided us with, available at the path "datasets/netflix_data.csv".
Print the first five rows of the DataFrame to inspect the data and ensure it was created successfully.
"""

#Read in the CSV as a DataFrame
netflix_df = pd.read_csv('netflix_data.csv')

#Print out the first five rows of the DataFrame
print(netflix_df.head())
