# Lists : ordered, mutable, allowa duplicate elements

# sort
mylist1 = [4, 3, 6, 9, -1, -5, 4]
print(mylist1)
mylist1.sort()
print("Sorted List ")
print(mylist1)
new_list1 = sorted(mylist1)
print("New List")
print(new_list1)

# contacatenaton and slicing
print("Concatenation")
concat_list = mylist1 + new_list1
print(concat_list)
# printing element for index 1 to 6
print(concat_list[1:6])
# printing element for index 0 to end of list
print(concat_list[0:])
# printing element with step sybtax list[begining index:ending index:step size]
print(concat_list[0:8:2])
# printing element for index last to begining
print(concat_list[::-1])

# list comprehension - way of creating list from existing list
list_comp = [i * i for i in mylist1]  # square of nos
print(list_comp)
[print(i) for i in list_comp] ##another way of printing via comperhension


# Tuples : ordered, immutable, allows duplicate elements
print("")
print("TUPLES")
print("creating tuples")
a1 = ("Tim", 23.2, 2, "Ron") #create new with rounded brackets
print(a1)

a2= tuple(concat_list) #from existing list
print(a2)

#extending list
print("Adding tuple to a list")
concat_list.extend(a1)
print(type(concat_list.extend(a1)))
print(concat_list)

