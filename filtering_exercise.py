
# Import the required libraries
import numpy as np 
import pandas as pd 

#Import the data from link
euro12 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")

#Select only the Goal Column
print(euro12.head())
#print(euro12['Goals'])

# How many teams participated in the Euro 2012?
print(euro12.shape) # 16 teams

# What is the number of columns in the dataset?
# 35 columns

# View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called Discipline
print(euro12.columns)

discipline = euro12.loc[:,['Team','Yellow Cards','Red Cards']]
#print(discipline)

# Sort the teams by Red Cards, then to Yellow Cards
discipline = discipline.sort_values(['Red Cards','Yellow Cards'],ascending = 'False')
print(discipline)

#Calculate the mean yellow Cards given per Team
print(discipline['Yellow Cards'].mean()) # 7.4

#Filter team that scored more than 6 goals
print(euro12[euro12['Goals'] > 6])

# Select the teams that start with G
print(euro12[euro12['Team'].str.startswith('G')])

# Select the first 7 columns
print(euro12.iloc[:,0:7])

# Select all columns except the last 3
print(euro12.iloc[:,:-3])

# Present only the shooting Accuracy from England, Italy and Russia
print(euro12.loc[euro12.Team.isin(['England','Italy','Russia']),('Team','Shooting Accuracy')])
