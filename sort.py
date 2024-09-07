def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for index in range(n - i - 1):
            if my_list[index] > my_list[index + 1]:
                my_list[index+1], my_list[index] = my_list[index], my_list[index+1]
    return my_list

def insertion_sort(my_list):
    for j in range(1,len(my_list)):
        temp = my_list[j]
        while(temp < my_list[j-1] and j>0):
            my_list[j] = my_list[j-1]
            j -= 1 
        my_list[j] = temp
    return my_list

def selection_sort(my_list):
    n = len(my_list)
    for index in range(n):
        min_val = my_list[index]
        for i in range(index+1,n):
            if my_list[i] < min_val:
                min_indx = i 
                min_val = my_list[i]
        if index != min_indx:        
            my_list[index], my_list[min_indx] = my_list[min_indx], my_list[index] 
                
    return my_list

def merge(list1, list2):
    merged_list = []
    i = 0 
    j = 0 
    while(i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            merged_list.append(list2[j])
            i += 1
            j += 1 
    if list1:
        merged_list.extend(list1[i:])
    if list2:
        merged_list.extend(list2[j:])
    
    return merged_list

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = len(my_list) // 2 
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)

def swap(index1, index2, my_list):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
    
def pivot(my_list, pivot_index, end_index):
    print("Inside piviot")
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        print(f"i: {i}, value { my_list[i]} pivot_index {pivot_index}, swap_index {swap_index}")
        
        if my_list[i] < my_list[pivot_index]:
            print(f"{my_list[i]} < {my_list[pivot_index]}")
            swap_index += 1
            print(f"swap_index {swap_index}")
            swap(swap_index, i,my_list)
    swap(pivot_index,  swap_index, my_list)            

    return swap_index

def quick_sort_helper(my_list, left, right):
    if left<right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index+1, right)
    return my_list
    
def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)
    
my_list = [1, 3, 8, 3,  2,3]
# print(bubble_sort(my_list))
# print(insertion_sort(my_list))
# print(insertion_sort(my_list))
# list1 = [1,3,4]
# list2 = [2,4,6]
# print(merge(list1, list2))
print(quick_sort(my_list))


