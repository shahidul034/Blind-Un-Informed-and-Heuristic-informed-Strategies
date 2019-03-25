def swap(str,a, b):
    str=list(str)
    temp = str[a]
    str[a] = str[b]
    str[b] = temp
    str1 = ''.join(str)
    return str1

def permutation(str,i,n):
    if i==n:
        print(str)
    else:
        for x in range(i,n+1):
            str=swap(str,i,x)
            permutation(str,i+1,n)
            str=swap(str,i,x)


str=input()
permutation(str,0,len(str)-1)