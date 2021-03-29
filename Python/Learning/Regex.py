#email address\text scraper
import re

text = "rnaAFSDKNSDNF"

pattern = re.compile("[a-zA-Z0-9]+")#here it will show everything a to z and lowe, upper and also numbers is matched.

result  = pattern.search(text)

print(result)