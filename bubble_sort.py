#Create a program that implements the bubble sort algorithm

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

my_arr = [6, 5, 2, 7, 1]
print(f'before the swap')
for i in range(len(my_arr)):
    print("% d" % my_arr[i], end=" ")

print(f'after the swap')
bubbleSort(my_arr)
for i in range(len(my_arr)):
    print("% d" % my_arr[i], end=" ")
