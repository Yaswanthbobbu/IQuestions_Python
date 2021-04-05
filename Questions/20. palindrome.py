str = input("enter the string:")

revstr=str[::-1]
print(revstr)

if str==revstr:
    print("palandrome")
else:
    print("not palindrome")
# # flag =0
# # for i in range(0,len(str)-1):
# #     if(str[i]==str[(len(str)-1)-i]):
# #         flag=1
# #     print("palindrome")



