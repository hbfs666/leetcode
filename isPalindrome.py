def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    temp = x
    flip = 0
    if (x < 0):
        return False
    while(temp>0):
        digit = temp % 10
        flip = flip * 10 + digit
        temp //= 10
    return (flip == x)

def main():
    print(isPalindrome(121))

main()
    
        