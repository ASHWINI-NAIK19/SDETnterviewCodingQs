#String Reverse using join() and reversed() function

def reverseStr(s):
    if len(s)==0:
        return s
    else:
        return ''.join(reversed(s))
print(reverseStr("hello"))
