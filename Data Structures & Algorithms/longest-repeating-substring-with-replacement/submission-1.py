class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,maxfreq=0,0
        maxlength=0
        counts={}
        for i in range(len(s)):
            counts[s[i]]=counts.get(s[i],0)+1
            maxfreq=max(maxfreq,counts[s[i]])
            while (i-left+1)-maxfreq >k:
                counts[s[left]]-=1
                left+=1
            maxlength=max(maxlength,(i-left+1)) 
        return maxlength       


