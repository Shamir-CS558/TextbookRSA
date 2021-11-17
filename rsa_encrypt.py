#Global Variables
e = 7 # The Constant Exponent
n = 0

def square_and_multiply(b, e, m):
    x = 1
    bits = list(bin(e)[2:])

    for bit in bits:
      x = (x * x) % m

      if (int(bit) == 1):
        x = (x * b) % m

    return x

def encrypt(message):
    ciphertext = square_and_multiply(message, e, n)
    print("Encrypted Message: ", ciphertext)
    return ciphertext

def main():
    global n

    #
    text = input("Enter the public key of the recipient: ")
    n = int(text, 16)

    # Message must be an Integer
    m = input("Enter a message: ")
    message = int(m)
    ciphertext = encrypt(message)


if __name__ == "__main__":
    main()
