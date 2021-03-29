list1 = [1,2,3,4,5,6]
list2 = ['one', 'two', 'three', 'four', 'five']
#it will truncate the last one like6 or six truncate = cut it off
zipped = list(zip(list1, list2))

#print(zipped)

#now unzip

unzipped = list( zip(*zipped))
#print(unzipped)

# for (l1, l2) in zip(list1,list2):
#   print(l1)
#   print(l2)

items = ['Apple', 'banana', 'orange']
counts = [3,6,4]
prices = [0.99, 0.25, 0.50]

sentences = []
for (item, count, price) in zip(items, counts, prices):
  item, count, price = str(item), str(count), str(price)
  sentence = 'I bought ' + count + ' ' + item + 's at ' + price + ' cents each.'
  sentences.append(sentence)
print(sentences)


#04:53:52