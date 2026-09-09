def pow(base , power):
    if power==0:
        return 1

    return base*pow(base, power-1)

print(pow(2,5))