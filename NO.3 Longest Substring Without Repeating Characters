class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        result = []
        for ch in list(s):
            if ch not in temp:
                temp.append(ch)
            else:
                if(len(temp) > len(result)):
                    result = temp[:]
                while(ch in temp):
                    temp.remove(temp[0])
                temp.append(ch)
        if(len(temp) > len(result)):
            result = temp[:]
        return ''.join(result)

temp = Solution()
a = 'jbpnbwwd'
print(temp.lengthOfLongestSubstring(a))
