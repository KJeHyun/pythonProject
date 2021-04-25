# append : 기존 리스트에 1개의 요소를 이어 붙이기
list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd', 'e']
list_1.append(6)
list_2.append('f')
print("append 6 for list_1 :", list_1)
# append 6 for list_1 : [1, 2, 3, 4, 5, 6]
print("append f for list_2 :", list_2)
# append f for list_2 : ['a', 'b', 'c', 'd', 'e', 'f']

# extend : 기존 리스트에 다른 리스트를 이어 붙이기 (+와 같음)
list_3 = [8, 9, 10]
list_1.extend(list_3)
print("extend list_3 to list_1 :", list_1)
# extend list_3 to list_1 : [1, 2, 3, 4, 5, 6, 8, 9, 10]

# count : 리스트 안에 object 가 몇 개 들어있는지 세어서 개수를 반환
print("count the number of in list_1 : ", list_1.count(3))
# count the number of in list_1 :  1

# index : 리스트에서 object 값이 있는 가장 작은 index 값 반환
print("show the index of 5 in list_1 : ", list_1.index(5))
# show the index of 5 in list_1 :  4

# insert : 기존 리스트의 index 위치에 obj 값을 삽입
list_1.insert(6, 7)
print("insert 7 in index 6 in list_1 : ", list_1)
# insert 7 in index 6 in list_1 :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pop : 기존 리스트에서 마지막 요소를 제거하고, 제거된 마지막 요소를 반환
list_1.pop()
print("pop from list_1 : ", list_1)
# pop from list_1 :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1.pop(7)
print("pop index 7 from list_1 : ", list_1)
# pop index 7 from list_1 :  [1, 2, 3, 4, 5, 6, 7, 9]

# sort : 리스트의 객체를 리스트 안에서 순서대로 정렬하기
list_4 = [3, 5, 1, 7]
list_4.sort()
print("sort list_4 : ", list_4)
# sort list_4 :  [1, 3, 5, 7]

# reverse : 리스트의 객체를 리스트 안에서 순서를 반대로 뒤집기
list_4.reverse()
print("reverse object 5 in list_4 : ", list_4)
# reverse object 5 in list_4 :  [7, 5, 3, 1]

# remove : 기존 리스트에서 obj 객체를 제거
list_4.remove(5)
print("remove object 5 in list_4 : ", list_4)
# remove object 5 in list_4 :  [7, 3, 1]

# clear : 기존 리스트에서 obj 객체를 모두 제거
list_4.clear()
print("clear list_4 : ", list_4)
# clear list_4 :  []

# copy : list 의 복사
list_4 = list_1.copy()
print("copy list_1 to list_4 : ", list_4)
# copy list_1 to list_4 :  [1, 2, 3, 4, 5, 6, 7, 9]

# len : 리스트 길이(object 수) 반환
print("length of list_1 : ", len(list_1))
# length of list_1 :  8

# max : 리스트 안에 있는 요소 중에서 최대값 반환
print("max of list_1 : ", max(list_1))
# max of list_1 :  9

# min : 리스트 안에 있는 요소 중에서 최소값 반환
print("min of list_1 : ", min(list_1))
# min of list_1 :  1

# list : 튜플/문자열을 리스트 자료형으로 변환
list_5 = list('hello')
print("list of hello : ", list_5)
# list of hello :  ['h', 'e', 'l', 'l', 'o']

# sorted : 정렬된 리스트를 새로운 리스트로 복사
list_6 = sorted(list_5)
print("sorted hello list : ", list_6)
# sorted hello list :  ['e', 'h', 'l', 'l', 'o']

# == : list1==list2(연산자 오버로드)
print("is list_5 same as list_6 : ", list_5 == list_6)
# is list_5 same as list_6 :  False

# string.split(character) : string 을 character 마다 끊어서 list 에 저장