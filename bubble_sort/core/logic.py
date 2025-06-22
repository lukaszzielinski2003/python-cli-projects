def bubble_sort_asc(nums: list[int]) -> None:
    """
    Sorting list in ascending order
    """
    n = len(nums)
    i = 0
    while i < len(nums) - 1:
        j = 0
        while j < n - i - 1:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j += 1
        i += 1
        print(f"Loop: {i}, {nums}")
    print(f"\nFinal sorted list: {nums}")


def bubble_sort_desc(nums: list[int]) -> None:
    """
    Sorting list in descending order
    """
    n = len(nums)
    i = 0
    while i < len(nums) - 1:
        j = 0
        while j < n - i - 1:
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j += 1
        i += 1
        print(f"Loop: {i}, {nums}")
    print(f"\nFinal sorted list: {nums}")
