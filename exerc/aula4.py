def zipper(l1, l2):
    interval = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(interval)]


l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(zipper(l1, l2))

print(list(zip(l1, l2)))
