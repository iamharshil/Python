import re

text = "rnaAFSDKNSDNF. MyName123@website.com . some more random text. Your_Name.8-8-8@company.net" #we need this mail id but it will pick first bcz it match.

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")#we can add -_ and other too
#for apply + in it use \+ for that

result  = pattern.search(text)#in this search will search only first function. for finding all use .findall

print(result)

#3:34:00