import pandas as pd

"""
Question 1:
What is the difference between the average cast size of a move and a tv show?
"""

Number_of_cast = dict()

titles = pd.read_csv("Questions/titles.csv")
credits = pd.read_csv("Questions/credits.csv")
print(credits.columns)
print(titles.columns)
