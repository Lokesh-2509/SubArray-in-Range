def get_subarray(arr, start_idx, end_idx):
    if start_idx < 0 or end_idx >= len(arr) or start_idx > end_idx:
        return []
    return arr[start_idx:end_idx + 1]
arr = [4, 3, 2, 6]
B = 1
C = 3
subarray = get_subarray(arr, B, C)
print("Subarray:", subarray)
arr = [4, 3, 2, 6]
B = 1
C = 3
subarray = get_subarray(arr, B, C)
print("Subarray:", subarray)
