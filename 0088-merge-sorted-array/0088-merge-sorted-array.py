class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1.extend(nums2)
        # nums1.sort()
        # a=0
        # for i in range(len(nums1)):
        #     if nums1[i] == 0:
        #         del nums1[i]
        #         a += 1
        # nums1.extend([0]*a)
        # return nums1

        i = m-1
        j = n-1
        k = m+n - 1

        #checking from end of two lists and placing the highest in the last of the given values by avoiding the filling values
        while i>=0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        
        while j >=0: 
            nums1[k] = nums2[j]
            k-=1
            j-=1
        #why because if there is only nums1=[1value] and no nums2, then direct print the nums1
        #so no i>=0: condition is needed

        return nums1



        