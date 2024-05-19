def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            # Точно знаходимо target, знаходимо upper_bound
            upper_bound = arr[mid]
            while mid + 1 < len(arr) and arr[mid + 1] == target:
                mid += 1
            if mid + 1 < len(arr):
                upper_bound = arr[mid + 1]
            return iterations, upper_bound
    
    # Якщо ми не знайшли точний елемент
    if left < len(arr):
        upper_bound = arr[left]
    
    return iterations, upper_bound

# Тестування функції
arr = [1.2, 1.5, 2.7, 3.6, 4.8, 5.9]
target = 3.6
print(binary_search(arr, target))  # Приклад, де елемент знайдено

target = 3.0
print(binary_search(arr, target))  # Приклад, де елемент не знайдено, але виведемо верхню межу
