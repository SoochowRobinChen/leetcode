test_list = [1, 2, 3, 4]
tuple_list = tuple(test_list)

print("list: ", test_list)
print("tuple: ", tuple_list)

test_list1 = [2, 3, 4, 5]
for i in range(len(test_list1)):
    print(str(test_list1[i]) + " and this is the index " + str(i) + " position")