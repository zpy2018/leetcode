class Solution(object):
    result = ''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                self.find(s, i, i+1)
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                self.find(s, i, i+2)
        if len(self.result) == 0 and len(s) > 0:
            self.result = s[0]
        return self.result[:]

    def find(self, s, head, tail):
        while head >= 0 and tail < len(s) and s[head] == s[tail]:
            head -= 1
            tail += 1
        head += 1
        if len(self.result) < tail - head:
            self.result = s[head:tail]
if __name__ == '__main__':
    temp = Solution()
    print(temp.longestPalindrome("b"))
