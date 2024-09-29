test_list = [1, 2, 3, 4]
tuple_list = tuple(test_list)

print("list: ", test_list)
print("tuple: ", tuple_list)

test_list1 = [2, 3, 4, 5]
for i in range(len(test_list1)):
    print(str(test_list1[i]) + " and this is the index " + str(i) + " position")


"""
what will return if we use python built-in split(' ')?

notice that there is difference between split() and split(' ')

"""

test_split_string = "      A    B  "
result_list = test_split_string.split()

print(result_list)