import random

# Author Shamir Ninja
# My Prototype of the Textbook RSA Implementation for sending encrypted messages

# If I keep e consistent across messages it will speed up encryption
# It may also allow for a simplier public key, only relying on sending N instead of (N,E)
e = 7

# Other global variables
n = 0
d = 0
didFindInverse = False


def find_primes(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

def extended_euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclid(b % a, a)
        return (g, x - (b // a) * y, y)

def multiplicative_inverse(a, m):
    global didFindInverse

    g, x, y = extended_euclid(a, m)
    if g != 1:
        didFindInverse = False
    else:
        didFindInverse = True
        return x % m

def rm_test(num):
   s = num - 1
   t = 0

   while s % 2 == 0:
      s = s // 2
      t += 1

   for tests in range(5):
      a = random.randrange(2, num - 1)
      v = pow(a, s, num)

      if v != 1:
         i = 0

         while v != (num - 1):
            if i == t - 1:
               return False
            else:
               i = i + 1
               v = (v ** 2) % num

      return True

def is_prime(num):
   if (num < 2):
      return False
   lowPrimes = list(find_primes(1024))

   if num in lowPrimes:
      return True
   for prime in lowPrimes:
      if (num % prime == 0):
         return False
   return rm_test(num)

# This key size should be secure for the foreseable future
def generate_prime(keysize = 1024):
   while True:
      num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
      if is_prime(num):
         return num

def generate_keys():
    primes = list(find_primes(1024))

    while (didFindInverse == False):
        global n
        global d

        p = generate_prime() #Choose random larger prime for p
        q = generate_prime() #Choose random larger prime for q
        n = p * q
        phi = (p - 1) * (q - 1)
        d = multiplicative_inverse(e, phi)

    print("-------------------YOUR 1024 BIT KEYS--------------------")
    print("Public key: ", hex(n))
    print("Private key: ", hex(d))

def main():
    generate_keys()

if __name__ == "__main__":
    main()
