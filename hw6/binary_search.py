def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [int(x) for x in input("Введите массив чисел через пробел: ").split()]
target = int(input("Введите искомое число: "))

result = binary_search(arr, target)
print("Индекс элемента {} : {}".format(target, result))
