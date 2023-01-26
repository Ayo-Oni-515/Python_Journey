# SEQUENTIAL/LINEAR SEARCH IN AN UNSORTED LIST (FOR LOOP)
my_list1 = [5,8,9,2,3,1,6,0,4,7]
my_list_comp = int(input("Enter a number between 0 and 9: "))
my_list_len = len(my_list1)
counter = 0
for i in my_list1:
    if my_list_comp != i:
        print("Data Not Found at index", counter)
    else:
        print("Data Found at index", counter)
    counter += 1

    
# SEQUENTIAL/LINEAR SEARCH IN AN UNSORTED LIST (WHILE LOOP)
my_list1 = [5, 8, 9, 2, 3, 1, 6, 0, 4, 7]
my_list_comp = int(input("Enter a number between 0 and 9: "))
my_list_len = len(my_list1)
found = False
counter = 0
position = 0
while counter < my_list_len and not found:
    data = my_list1[position]
    if my_list_comp == data:
        print("Data Found at index", counter)
        found = True
    counter += 1
    position += 1
