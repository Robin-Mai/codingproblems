def fixed_sliding_window(arr, k):
    result = list()
    current_sub = sum(arr[:k])
    result = [current_sub]

    for i in range(1, len(arr)-k+1):
        current_sub = current_sub - arr[i-1]
        current_sub = current_sub + arr[i+k-1]

        result.append(current_sub)
    return result

def dynamic_sliding_window(arr, x):
    #find minimum length subarray with minimum sum of x
    start = 0
    end = 0
    current_sum = 0
    min_length = float('inf')

    while end < len(arr):
        current_sum += arr[end]
        end = end + 1

        while start < end and current_sum >= x:
            current_sum = current_sum - arr[start]
            start = start + 1

            min_length = min(min_length, end - start + 1)
    return min_length


arr = [1, 2, 3, 4, 5, 6]
#[1, 2, 4, 7, 1, 8, 8, 2]
res = fixed_sliding_window(arr, 3)
max = max(res)
print(max)

res = dynamic_sliding_window(arr, 7)
print(res)