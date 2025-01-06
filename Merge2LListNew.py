from collections import deque

def mergeTwoLists(list1: deque, list2: deque) -> deque:
    merged_list = deque()

    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.popleft())
        else:
            merged_list.append(list2.popleft())

    # Append any remaining elements from either list
    merged_list.extend(list1)
    merged_list.extend(list2)

    return merged_list

# Example usage
list1 = deque([1, 2, 4])
list2 = deque([1, 3, 4])

merged_list = mergeTwoLists(list1, list2)
print(list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]
