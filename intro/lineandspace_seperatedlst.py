# line sepearted lists
'''li = []
n = int(input())
for i in range (n):
    curr = int(input())
    li.append(curr)
print(li)'''
# space sepearted list
n = int(input())
li = [int(x) for x in input().split()]
for ele in li:
    print(ele)