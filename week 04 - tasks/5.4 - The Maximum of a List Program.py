def maximun(x,y):
    if x > y:
        return x
    else:
        return y


def max_list(num_list):
    current_max = num_list[0]
    for x in num_list[1:]:
        current_max = maximun(current_max, x)
    return current_max


list_one = [3,6,2,1,8,4,4,2,7]
list_two = [30,16,4,45,27,84]
list_three = [-10,-4,-3,-2]

print(f"Maximum of list 1 is {max_list(list_one)}")
print(f"Maximum of list 1 is {max_list(list_two)}")
print(f"Maximum of list 1 is {max_list(list_three)}")