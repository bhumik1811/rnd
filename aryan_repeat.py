list1= [1, 2, 3, 4 ]
list2 = list1

print(list1)
print(list2)

list2.append(6)
print(list1)
print(list2)

list3 = list1[:]
print("list1", list1)
print("list3",list3)
list3.append(67)

print("after apppend list1", list1)
print("after append list3",list3)

#varibale assignment
a = 10
b = 20
#print (a,b)
#c = a
#a = b
#b = c
#print(a , b)
print(a, b)
a, b = b, a
print(a, b)

list= [10,6,8,2]

#swapped = True
'''while swapped:
    swapped = False
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            swapped= True
            list[i], list[i+1]= list[i+1],list[i]
print(list)'''


list.sort()

print(list)
list.reverse()
print(list)













