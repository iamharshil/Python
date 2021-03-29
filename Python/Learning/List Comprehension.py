names = ['jannie', 'jaref', 'jazzy', 'james']

#for change that list into new list
l = []
for person in names:
  l.append(person)
print(l)
#or
#you can use that for loop or this comprehesion for same thing.
print([person for person in names])

#EX
l = []
for person in names:
  l.append(person + ' dumped me.')
print(l)

#or
print([person + ' dumped me.' for person in names])


Movies_and_ratings = {"Interseller":9, "dark Night":8, "50 shades":3, "50 shades Darker":2}

l = []
for movie in Movies_and_ratings:
  if Movies_and_ratings[movie] > 6:
    l.append(movie)
print(l)
#or
print( [movie for movie in Movies_and_ratings if Movies_and_ratings[movie] >6] )

#3:14:04