class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Original idea::
        # first move right most k elements of nums in to a new list/array
        # then prepend each to front of the nums
        Doesn't work because k can be larger than the length of nums
        """
        #Then a easy but not time efficient way popped up in my mind
        #just use a for loop to pop the last element and insert it to the front of the array for k times
        #This is not time efficient because the time complexity is O(n*k)
        #but very space efficient because space complexity is O(1)
        for i in range(0, k):
            nums.insert(0, nums.pop())
