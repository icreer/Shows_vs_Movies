import pandas as pd
from numpy import loadtxt

"""
Question 1:
What is the difference between the average cast size of a move and a tv show?
"""

Number_of_cast = dict()

titles = pd.read_csv("Questions/titles.csv")
credits = pd.read_csv("Questions/credits.csv")
#print(credits.columns)
#print(titles.columns)

IDtitles = titles.columns[0]
IDcredit = credits.columns[1]
'''
More just testing pandas
'''

"""
if titles.columns[0] == credits.columns[1]:
    print(IDcredit)
    print(IDtitles)

print(titles["id"])
print(credits["id"])
"""

#credits["id"].value_counts().to_csv("resalts.txt", sep= " ", index=True)
#titles[["id","type"]].to_csv("shows.txt", sep = " ",index = False)

'''
Used to check if the resalt file is true
'''
#print(titles.dtypes)
#print(credits.dtypes)
#print(credits["id"].value_counts())
#print(titles[["id","type"]])

cast_value = loadtxt("resalts.txt",str)
titles_type = loadtxt("shows.txt",str)

cast_id = cast_value[:,0]
cast_number = cast_value[:,1]

titles_id = titles_type[:,0]
titles_moveorshow = titles_type[:,1]

print(cast_id)
print(cast_number)
print(titles_id)
print(titles_moveorshow)


map_of_id_and_cast_number = dict()
map_of_id_and_moveorshow = dict()

for i in range(len(cast_id)):
    #print(cast_id[i]+","+cast_number[i])
    map_of_id_and_cast_number[cast_id[i]] = cast_number[i]

for i in range(len(titles_id)):
    map_of_id_and_moveorshow[titles_id[i]] = titles_moveorshow[i]

"""
This my frist attepmt to get an average but they are very 
"""
show_amount = 0
show_count_cast = 0
movie_amount = 0
movie_count_cast = 0

for title in map_of_id_and_cast_number:
    if title in map_of_id_and_moveorshow:
        if map_of_id_and_moveorshow[title] == "MOVIE":
            movie_amount +=1
            movie_count_cast += int(map_of_id_and_cast_number[title])
        elif map_of_id_and_moveorshow[title] == "SHOW":
            show_amount += 1
            show_count_cast += int(map_of_id_and_cast_number[title])

print(f"The number of show is {show_amount}.")
print(f"The number of cast members for shows is {show_count_cast}")
print(f"The number of movies is {movie_amount}")
print(f"The number of cast members for movie is {movie_count_cast}")

average_movie_cast_amount = movie_count_cast / movie_amount
average_show_cast_amount = show_count_cast / show_amount

print(average_movie_cast_amount)
print(average_show_cast_amount)