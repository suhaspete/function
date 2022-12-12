# #first n natural no
# n = int(input())
# count =1   
# while count<=n :
#     print(count)
#     count = count+1
#print 1 for n times
# n = int(input())
# count = 1
# while count<=n:
#     print(1)
#     count += 1
#print sum of even numbers
# n = int(input())
# i = 0
# sum = 0
# while i<=n :
#     sum += i
#     i+=2

# print(sum)
# check prime no 
n = int(input())
d= 2
flag = True
while d<n :
    if(n%d==0) :
        flag = True
        d = d+1
if flag :
    print('not prime no')
else :
    print('prime no')  