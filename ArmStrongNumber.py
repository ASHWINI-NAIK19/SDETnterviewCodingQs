#You are given a 3-digit number n, Find whether it is an Armstrong number or not
#Input: n = 153
#Output: true
#Explanation: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153.

def isarmStrong():
    n=int(input("Enter number:"))
    ar=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum+r**3
        n=n//10
    if ar==sum:
        return True
    else:
        return False
print(isarmStrong())
