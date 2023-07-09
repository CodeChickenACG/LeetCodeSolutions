class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #use a dict to store number of an element appear in the array
        #then iterate the dict, if an element has a val >n/2 then return the val
        num_times=dict()
        i=0
        while i < len(nums):
            if nums[i] not in num_times.keys():
                num_times[nums[i]] = 1
                #print(num_times)
            else:
                num_times[nums[i]] += 1
                #print(num_times)
            i+=1
        for j in num_times:
            if num_times[j] > len(nums)/2 :
                return j