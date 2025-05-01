#You are given a 3-digit number n, Find whether it is an Armstrong number or not
#Input: n = 153
#Output: true
#Explanation: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153
#Input: 1634
#Output: Yes
#Explanation: 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 = 1634

def isarmStrong():
    n=int(input("Enter number:"))
    pw=len(str(n))
    ar=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum+r**pw
        n=n//10
    if ar==sum:
        return True
    else:
        return False
print(isarmStrong())
