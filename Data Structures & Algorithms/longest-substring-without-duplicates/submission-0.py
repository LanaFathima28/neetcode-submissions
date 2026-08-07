class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        maxlength=0
        last_seen={}
        for i in range(len(s)):
          
          if s[i] in last_seen and left<=last_seen[s[i]]:
            left=last_seen[s[i]]+1
          last_seen[s[i]]=i
          length=i-left+1
          maxlength=max(maxlength,length)
        return maxlength  