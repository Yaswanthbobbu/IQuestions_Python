import re

str="Enter spl characters"
regX =re.compile('!@# $ %^&*()_+{};:"/\|')


if(regX.search(str)==None):
    print("Contains spl characters")
else:
    print("Contains No spl characters")

