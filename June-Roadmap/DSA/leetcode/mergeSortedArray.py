## merging sorted array
def merge(nums1, m, nums2, n):
    # last element
    last = m + n - 1
    #merge in reverse order
    while m > 0 and n > 0:
        if nums1[m] > nums2[n]:
            nums1[last] = nums2[n]
            m -= 1
        else:
            nums1[last] = nums2[m]
        last -= 1    
