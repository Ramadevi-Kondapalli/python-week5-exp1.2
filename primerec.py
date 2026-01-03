def is_prime_rec(n,i=2):
    if n<=1:
        return False
    if n==i:
        return True
    if n%i==0:
        return False
    return is_prime_rec(n,i+1)
num=int(input("enter a number:"))
if is_prime_rec(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
