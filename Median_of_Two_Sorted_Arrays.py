nums1 = [1, 2]
nums2 = [3, 4]

new = nums1 + nums2
result = 0
if len(sorted(new)) % 2 == 0:
    result = (sorted(new)[len(sorted(new)) // 2] + sorted(new)[len(sorted(new)) // 2 - 1]) / 2
else:
    result = sorted(new)[len(sorted(new)) // 2]
print(result)
