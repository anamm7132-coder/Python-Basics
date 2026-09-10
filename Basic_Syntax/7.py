def counter(str,ch):
    i=0
    count=0
    while(i<len(str)):
        find=str[i]
        if find==ch:
            count+=1
        i+=1
    return count

print(counter("My name is Anam",'a'))
