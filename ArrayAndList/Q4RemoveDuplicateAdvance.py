class Solution:
    #This question is similar to Q3, but the difference is the allowed duplicate element is up to 2
    #and return the length of the array that has max of 2 duplicate element
    #First we use a dictionary to store the unique element in the array, dict can track how many times the element appears
    #Then we use a pointer to point to the element in the array
    #if the element is not in the dict, add it to the dict and increment the counter
    #if the element is in the dict and the value of the element is less than 2,
    #increment the value of the element in the dict and increment the counter
    #if the element is in the dict and the value of the element is equal or greater than 2,
    #replace it with a number bigger than input limit
    #in this case, <=10^4, so 10^4+1 satisfies the condition
    #sort the array


    def removeDuplicates(self, nums: List[int]) -> int:
        #use dictionary
        count=0
        exist=dict()
        i=0
        while i < len(nums):
            if nums[i] not in exist.keys():
                exist[nums[i]]=1
                count+=1
            elif nums[i] in exist.keys() and exist[nums[i]]<2:
                exist[nums[i]] += 1
                count+=1
            else:
                nums[i] = 10**4+1
            i+=1
        nums.sort()
        return count