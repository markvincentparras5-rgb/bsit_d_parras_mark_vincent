# Activity 6: Recursive Array Toolkit

def sum_array(arr, i=0):
    if i == len(arr):
        return 0

    return arr[i] + sum_array(arr, i + 1)


def find_largest(arr, i=0):
    if len(arr) == 0:
        raise ValueError("Array must not be empty.")

    if i == len(arr) - 1:
        return arr[i]

    largest_rest = find_largest(arr, i + 1)

    if arr[i] > largest_rest:
        return arr[i]
    else:
        return largest_rest


def count_number(arr, target, i=0):
    if i == len(arr):
        return 0

    if arr[i] == target:
        return 1 + count_number(arr, target, i + 1)
    else:
        return count_number(arr, target, i + 1)



print("1. SUM THE ARRAY")
print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4, 5]))
print(sum_array([-2, 5, -3, 10]))


print("\n2. FIND THE LARGEST NUMBER")
print(find_largest([8]))
print(find_largest([10, 5, 3, 2]))
print(find_largest([1, 2, 3, 15]))
print(find_largest([-10, -5, -2, -8]))


print("\n3. COUNT A CHOSEN NUMBER")
print(count_number([], 5))
print(count_number([2, 5, 5, 3, 5], 5))
print(count_number([1, 2, 3, 4], 7))