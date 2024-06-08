class Solution(object):
    def repeatedSubstringPattern(self, s):
        if (len(s)%2==1):
            return False
        n= 2
        while (n<(len(s)//2)):
            sub = s
            sub = sub[:len(sub)//n]
            if (sub*n == s):
                return True
            n+=1
        return False