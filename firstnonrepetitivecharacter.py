#Program to display first non- repetitive character in string
#input="geeksforgeeks"
#output=f

def rep():
    st=input("Enter the string:")
    for i in range(len(st)):
        flag=0
        for j in range(len(st)):
            if i!=j and st[i]==st[j]:
                flag=1
                break
        if flag==0:
            print("First non- repetitive character in string:",st[i])
            break
    if flag==1:
        print("repeating characters present")
  
rep()
