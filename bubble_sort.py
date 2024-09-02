def bubble_sort(my_list):
    for n in range(len(my_list)):
        for index in range(len(my_list)-1):
            if my_list[index] > my_list[index + 1]:
                my_list[index+1], my_list[index] = my_list[index], my_list[index+1]
        print(my_list)
    return my_list

my_list = [1, 6, 8, 3, 4, 3]
print(bubble_sort(my_list))