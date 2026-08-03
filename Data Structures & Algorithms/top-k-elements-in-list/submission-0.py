class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for num in nums:
           freq[num]=freq.get(num,0)+1
        sorted_freq=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        for key in sorted_freq:
            result.append(key)
            if len(result)==k:

               return result    