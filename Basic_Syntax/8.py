def sumofdig(num):
    if num==0:
        return 0

    return sumofdig(num//10)+num%10

print(sumofdig(5324))