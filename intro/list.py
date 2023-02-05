li = [1,2,5,90,86,'suhas']
print(type(li))
li = [2,7,9,1,2,5,90,86,'suhas','suhas']
print(li)
li [0] = 8
li [0] = 89
print(li)
print(li[0:1])
print(li[1:])
print(li[0:10])
li.insert(1,0)
print(li[0:10])
li.append([29,2589,'suhas'])
print(li)
li.extend([29,2589,'suhas'])
print(li)
# remove func it will remove what we type ,for ex if two 5's are prensent then it remove 1st 5 ok
li.remove(1)
print(li)
li.remove('suhas')
print(li)
#li.remove('tt')
# pop func it will remove what we type ,for ex if two 5's are prensent then it remove last 5 ok
li.remove('suhas')
print(li)
li.remove(2)#index it will remove that index)
len(li)
print(len(li))
print(li)
li.pop(7)
print(li)
print(li.pop(1))
print(li)
