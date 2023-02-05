'''n = int(input())
for i in range (2,n+1,2):
   if i %7==0 :
    continue
    print(i)'''
#2
n = int(input())
for i in range(2,n+1,2):
    print(i)
    if i%7==0:
        continue
    print(i)