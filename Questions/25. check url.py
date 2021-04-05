import re

url = "https://urlregex.com"
str = " i search at https://bing.com and the https://urlregex.com"

url2= re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",str)
print(url2)

