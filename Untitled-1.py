def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    temp = x
    flip = 0
    while(temp>0):
        i = 1
        digit = temp % 10
        temp /= 10
        flip += digit*i
        i+1
    return (flip == x)

def main():
    print(isPalindrome(121))

main()
    
        