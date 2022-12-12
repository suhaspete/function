a = int(input())
b = int(input())
if(a%3==0) :
    for i in range(a,b+1,3):
      print(i)
elif(a%4==0):
    a= a+2
    if(a%3==0) :
     for i in range(a,b+1,3):
      print(i)
elif(a%5==0):
    a= a+1
    if(a%3==0) :
       for i in range(a,b+1,3):
         print(i)
elif(a%2==0):
    a= a+1
    if(a%3==0) :
       for i in range(a,b+1,3):
         print(i)

