import pandas as pd
from numpy import loadtxt
import matplotlib.pyplot as plt

"""
Question 2:
What is the average age of content and what is the trend?
"""
titles = pd.read_csv("Questions/titles.csv")
credits = pd.read_csv("Questions/credits.csv")

#titles["release_year"].value_counts().to_csv("release.txt",sep=" ", index=True)

release_year = loadtxt("release.txt", int)

years = release_year[:,0]

number_of_releases = release_year[:,1]

maping_release_year_data = dict()

for i in range(len(years)):
    maping_release_year_data[years[i]] = number_of_releases[i]

total_number_of_releases = 0
current_year = 2022
weightavergesnumerater = 0
age = []

for i in range(len(number_of_releases)):
    age.append(current_year - number_of_releases[i])
    total_number_of_releases += number_of_releases[i]
    weightavergesnumerater += number_of_releases[i] * (current_year-years[i])

weightaverge = weightavergesnumerater/total_number_of_releases
print(f"The average age of a movie or show on netfix is {weightaverge}")

plt.stem(years,number_of_releases )
plt.title("Number of new content on Netflix each year")
plt.xlabel("Years")
plt.ylabel("Number of Movie or Shows")
plt.show()