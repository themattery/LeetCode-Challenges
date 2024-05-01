# Turn value into string & compared to its 
# reversed version by using string manipulation

class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        reversedValue = value[::-1]
        if reversedValue == value:
            return True
        else:
            return False

        