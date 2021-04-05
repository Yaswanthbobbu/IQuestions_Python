list=["geeks",3,4,"geeks","geeks",3,5]
word = "geeks"
n=1
count=0
size=len(list)-1
for i in range(0,size):
    if word == list[i]:
        count+=1
        if(count==n):
            del list[i]
print(list)