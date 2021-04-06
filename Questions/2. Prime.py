num1 = input("Enter number: ")

count =0
if num1 > 0 :
 for i in range(1,num1+1):
     if (a%i) == 0:
         count+=1
 if count == 2:
     print("Not prime")
 else :
     print("prime")