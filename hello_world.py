def prime(n):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
    return prime
li=[2,4,3,5,6,7]
print(list(filter(prime,li)))
print("This is the first pushed project of mine in gihub")
