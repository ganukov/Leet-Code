def two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        result = target - num

        if result in num_dict:
            return [num_dict[result], i]

        num_dict[num] = i

    return []