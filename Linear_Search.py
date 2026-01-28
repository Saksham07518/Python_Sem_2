list = eval(input("Enter a list of numbers :"))
target = int(input("Enter the number to be searched :"))

# for i in range(len(list)):
#     if list[i] == target:
#         print(f"Element {target} found at index : {i}")
#         break
# else:
#     print(f"Element not found in the list")

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1
result = linear_search(list, target)
print(result)

