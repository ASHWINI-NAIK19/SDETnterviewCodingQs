#String Reverse through loop without using slicing 


def reverseStr(s):
    rev=''
    for ch in range(len(s)-1,-1,-1):
        rev=rev+s[ch]
    print("Reversed String is:",rev)
reverseStr(input("Enter some string:"))
