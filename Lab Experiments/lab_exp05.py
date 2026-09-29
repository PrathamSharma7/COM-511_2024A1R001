'''
5. Write a program to perform searching activity using linear and binary search.
'''

print("-----Linear Search-----")
numbers = list(map(int,input("Enter a numbers: ").split()))
target = int(input("Enter target to search: "))
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f" {target} Found at index {i}\n")
        break
else:
    print(f"{target} not found in the list\n")

print("-----Binary Search-----")
sorted_numbers = list(map(int,input("Enter a numbers in sorted order: ").split()))
target = int(input("Enter target to search: "))
left = 0
right = len(sorted_numbers) - 1
while left <= right:
    mid = (left + right) // 2
    if sorted_numbers[mid] == target:
        print(f" {target} Found at index {mid}\n")
        break
    elif sorted_numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f"{target} not found in the list\n")