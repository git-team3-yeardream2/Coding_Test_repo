def ispalindrome(s):
    def tochar(s):
        s = s.lower()
        ans = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + char
        return ans
    def ispal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])
    return ispal(tochar(s))

print(ispalindrome('abccba'))
