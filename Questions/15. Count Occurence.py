list=[1,2,3,4,5,6,6,6,6,7,8]
n=6
count=0

 for i in list:
    if(i==n):
        count+=1
 print(count)
 print("{} has occurred {} times".format(n,count))
# #count method
print("{} has occurred {} times".format(n,list.count(n)))
#counter
 from collections import Counter
 dic=Counter(list)
print("{} has occurred {} times".format(n,dic[n]))
