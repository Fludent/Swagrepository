# prime or no prime
import sys

print("Enter a number:")
n = int(input())

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def big_prime(n):
    while (is_prime(n) == False):
        n += 1
    return n


def small_prime(n):
    while (is_prime(n) == False):
        n -= 1
    return n
numb = is_prime(n)
bot = small_prime(n)
top = big_prime(n)

if (numb == True):
        print n,"is prime."
        sys.exit()
print((str(bot)) + " < " + str(n) + " < " + str(top))
