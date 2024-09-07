# functions to list the first N prime numbers

num = int(input("Enter a number: "))

def prime(num):
    flag = 1
    if(num < 0):
        try:
            raise Exception("Enter a positive integer")
        except Exception as e:
            print(e)
    else:
        for i in range(2, num):
            if num % i == 0:
                flag = 0
        if flag == 0:
            return False
        return True

primes = []
def nPrime(num):
    for i in range(1,num):
        if(prime(i)):
            primes.append(i)
    return primes

# print(nPrime(num))

# Matrix multiplication




