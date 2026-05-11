def merge_sorted_array(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i = i - 1
        else:
            nums1[k] = nums2[j]
            j = j - 1
        k = k - 1

    while j >= 0:
        nums1[k] >= nums2[j]
        j = j - 1
        k = k - 1
    return nums1
print(merge_sorted_array([1,2,3,0,0,0], [2,5,6], 3, 3))    