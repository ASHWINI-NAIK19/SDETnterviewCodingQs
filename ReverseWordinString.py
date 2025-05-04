#Reverse the string in such a way that words should be reversed not complete string
#hello world
#world hello

def revWord():
    s=input("Enter string:")
    st=s.split()
    rev=" ".join(st[::-1])
    print(rev)
revWord()
