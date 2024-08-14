list_a = [1, 2, 3, 4, 5]
list_b = [2, 3, 4, 5, 6, 7, 8]

sum_list = [x+y for x, y in zip(list_a, list_b)]
print(sum_list)


sum_list_for = []
for i, _ in enumerate(list_a):
    sum_list_for.append(list_a[i] + list_b[i])
print(sum_list_for)
