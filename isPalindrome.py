def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    temp = x
    flip = 0
    i = 0
    while(temp>0): 
        digit = temp % 10
        temp = temp // 10
        flip += digit*10**i
        i += 1
    return (flip == x)

def main():
    print(isPalindrome(121))

main()
    
        