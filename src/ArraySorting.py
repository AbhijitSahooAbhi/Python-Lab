array = int(input("Enter Size of Array:"))
arr = []

for i in range(array):
    element = int(input(f"Enter element {i+1}:"))
    arr.append(element)

arr.sort()

print("Sorted Array:", arr)