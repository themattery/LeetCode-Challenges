# Solution using a pointer that reads the string in reverse
# by comparing the current value w/ the previous one,
# then effecting the proper operation (+ or -) and storing 
# the result. I may try using the reverse function next time
# for optimization

class Solution:
    def valueOf(self, x: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return symbols[x]
    
    def romanToInt(self, s: str) -> int:
        pointer = len(s)-1

        result = self.valueOf(s[pointer])

        while pointer>0:
            value = self.valueOf(s[pointer])
            previousValue = self.valueOf(s[pointer-1])
            if value > previousValue:
                result-=previousValue
            else:
                result+=previousValue
            pointer-=1
        return result
        