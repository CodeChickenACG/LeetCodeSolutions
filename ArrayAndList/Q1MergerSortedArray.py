class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #setting two pointers j and i
        #j is for nums2(second array input) and i is for nums1(first array input)
        #if the placekeeper element "0" is found in nums1, replace it with the element in nums2
        #increment j and i to move to the next element and prevent infinite loop
        #sort the array
        #This quqestion don't need to return anything, so just modify nums1 in-place
        j = 0
        i=0
        while i<m+n and j <n:
            print(i)
            print(j)
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                print(nums1)
                j+=1
            i+=1
        nums1.sort()
