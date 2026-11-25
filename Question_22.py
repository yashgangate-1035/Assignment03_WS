#Write a function to return all factors of a number.

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

num = int(input("Enter a number: "))
print(get_factors(num))
