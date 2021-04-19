# append
list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd', 'e']
list_1.append(6)
list_2.append('f')
print("append 6 for list_1 :", list_1)
print("append f for list_2 :", list_2)
# extend
list_3 = [8, 9, 10]
list_1.extend(list_3)
print("extend list_3 to list_1 :", list_1)
print("count the number of in list_1 : ", list_1.count(3))
# index
print("show the index of 5 in list_1 : ", list_1.index(5))
# insert
list_1.insert(6, 7)
print("insert 7 in index 6 in list_1 : ", list_1)
# pop
list_1.pop()
print("pop from list_1 : ", list_1)
list_1.pop(7)
print("pop index 7 from list_1 : ", list_1)
# sort
list_4 = [3, 5, 1, 7]
list_4.sort()
print("sort list_4 : ", list_4)
# reverse
list_4.reverse()
print("reverse object 5 in list_4 : ", list_4)
# clear
list_4.clear()
print("clear list_4 : ", list_4)
# copy
list_4 = list_1.copy()
print("copy list_1 to list_4 : ", list_4)
