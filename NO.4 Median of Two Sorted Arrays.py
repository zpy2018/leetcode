class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        i1 = i2 = 0
        if(len(nums1) == 0 or len(nums2) == 0):
            result = nums1 + nums2
        else:
            for i in range(len(nums1) + len(nums2)):
                if(i1 == len(nums1)):
                    result = result + nums2[i2:]
                    break
                if (i2 == len(nums2)):
                    result = result + nums1[i1:]
                    break
                if(nums1[i1] <= nums2[i2]):
                    result.append(nums1[i1])
                    i1 += 1
                else:
                    result.append(nums2[i2])
                    i2 += 1
        if(len(result) % 2 == 0):
            rnum = (result[len(result)//2] + result[len(result)//2 - 1])/2.0
        else:
            rnum = result[(len(result) - 1) // 2]
        return rnum

temp = Solution()
n1 = [1,2]
n2 = [3,4]
print(temp.findMedianSortedArrays(n1, n2))

