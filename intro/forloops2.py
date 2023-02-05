#1
'''n = int(input())
for i in range(0,n+1,1):
    print(i)
#2
n = int(input())
for i in range(n+1):
    print(i)
#3
n = int(input())
for i in range(1,n+1):
    print(i)
#4
n = int(input())
for i in range(n,0,-1):
    print(i)'''
    #5 multiples of 3
'''a = int(input())
b = int(input())
for i in range(a,b+1,1):
  if(i%3==0):
    print(i)'''
# or from above
'''a = int(input())
b = int(input())
if(a%3==0):
    s = a
elif(a%3==1):
    s=a+2
elif(a%3==2):
    s= a+1
for i in range(s, b+1,3):
    print(i)'''
    #prime or no slow 
n = int(input())
flag = False
for d in range( 2, n, 1):
    if n%d==0:
        flag = True
        
if flag :
    print("not prime no")
else :
    print('prime')
# prime or no very fast
n = int(input())
flag = False
for d in range( 2, n, 1):
    if n%d==0:
        flag = True
        break
if flag :
    print("not prime no")
else :
    print('prime')

