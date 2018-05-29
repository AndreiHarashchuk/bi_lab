# 1
list1 = [1, 2, 3]

list2 = [a + b for a in 'ab' for b in 'bcd']
print(list2)

# 2
sliced_list2 = list2[::2]
print(sliced_list2)

# 3
list3 = [str(c) + 'a' for c in range(1, 5)]
print(list3)

# 4
print(list3.pop(1))

# 5
list3.append('2a')
print(list3)
