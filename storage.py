import csv

all_movies = []

with open('final.csv','r', encoding="ISO-8859-1") as f:
    reader = csv.reader(f,skipinitialspace = True)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []