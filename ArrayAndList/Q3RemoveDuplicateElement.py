class Solution:
    #This question is similar to Q2, but the difference is that we need to remove the duplicate element in the array
    #and return the length of the array that has no duplicate element
    #First we use a set to store the unique element in the array
    #Then we use a pointer to point to the element in the array
    #if the element is not in the set, add it to the set and increment the counter
    #if the element is in the set, replace it with a number bigger than input limit
    #in this case, <=100, so 101 satisfies the condition
    #sort the array

    def removeDuplicates(self, nums: List[int]) -> int:
        #use set
        count=0
        exist=set()
        i=0
        while i < len(nums):
            if nums[i] not in exist:
                exist.add(nums[i])
                count+=1
            else:
                nums[i] = 101
            i+=1
        nums.sort()

        return count