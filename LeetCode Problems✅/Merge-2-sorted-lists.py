list1 = []
list2 = [3]
final_list = []

def merege_two_sorted_list():
    for i in range(len(list1)):
        final_list.append(list1[i])
    for j in range(len(list2)):
        final_list.append(list2[j])
    return final_list
print(merege_two_sorted_list())