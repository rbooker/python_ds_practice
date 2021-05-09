def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_count_dict = {nums.count(x):x for x in nums}
    num_counts = list(num_count_dict.keys())
    num_counts.sort()
    return num_count_dict.get(num_counts[-1])
