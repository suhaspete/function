#avg
'''a = int(input('enter the first digit'))
b = int(input())
c = int(input())
result = (a+b+c)/2
print(result)'''
#reverse manner
'''n =int(input())
rev =0
while(n!=0) :
        digit=n%10
        rev = (rev*10)+digit
        n = n%10
print(rev)'''
#100-200 sum of even digits
'''sum = 0
for i in range(11):
    sum = sum +i
print(sum)'''
'''sum = 0
for i in range(4):
    if(i%2!=0):
       sum = sum +i
print(sum)'''
#
s1 = int(input())
s2 = int(s1[::-1])
if s2==s1 :
    print('true')
else :
    print('false')
