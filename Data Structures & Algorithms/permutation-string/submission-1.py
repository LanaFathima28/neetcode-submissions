class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorteds1=''.join(sorted(s1))
        n=len(s1)
        for i in range(len(s2)-(n-1)):
            s3=''.join(sorted(s2[i:i+n]))
            if s3==sorteds1:
                return True
        return False         