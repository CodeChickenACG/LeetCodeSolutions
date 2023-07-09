class Solution:
    #This question is similar to Q1, but the difference is that we need to remove the element in the array
    #and return the length of the array
    #So, we need to set a counter to count the number of elements in the array
    #and set a pointer to point to the element in the array
    #if the element is equal to the target, replace it with a number bigger than input limit
    #in this case, <=50, so 51 satisfies the condition
    #increment the counter
    #sort the array
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i= 0
        while i < len(nums):
            if nums[i] == val:
                nums[i]=51
            else:
                count+=1
            i+=1
        nums.sort()
        return count