# n = int(input())
# li = [int(x) for x in input().split()]
# ele = int(input())
# isFound = False
# for i in range (len(li)):
#     print(i)
#     isFound=True
#     break
# if isFound is False:
#     print(-1)
# # through func
# def linear_search(li,ele):
#     for i in range (len(li)):
#         if li[i]==ele:
#             return 1
#     return -1
# li = [1,2,3,6,5]
# index=linear_search(li,9)
# print(index)
#    #binary search
li = [1,3,7,18,20,21,28,32]
for i in range(len(li)):
    if li[i] == li[len(li)-1]:
        i+=1
print(li(i))
    