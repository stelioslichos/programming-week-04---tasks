import copy


def update_list_item_one(l, x):
    l.pop(0)
    l.insert(0, x)


def new_list_item_one(l, x):
    new_list = copy.copy(l)
    new_list.pop(0)
    new_list.insert(0, x)
    return new_list

l = [1,2,3,4]
update_list_item_one(l, 0)
print(l) # prints out [0,2,3,4]

l = [1,2,3,4]
new_list_item_one(l, 0)
print(l) # prints out [1,2,3,4]

l = [1,2,3,4]
l = new_list_item_one(l, 0) # bind the new object to l
print(l) # prints out [0,2,3,4]