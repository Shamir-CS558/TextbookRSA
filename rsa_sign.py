from hashlib import sha512

#Global variables
d = 0 #Private Key 103
n = 0 #Public Key  169
e = 7 #Constant exponent

def sign():
    global d
    global n

    pubkey_str = input("Enter your public key: ")
    n = int(pubkey_str)
    privkey_str = input("Enter your private key: ")
    d = int(privkey_str)

    msg = input("Enter the message you wish to sign: ").encode('utf8')
    hash = int.from_bytes(msg, byteorder='big')
    signature = pow(hash, d, n)
    print("Message Signature:", hex(signature))

def main():
    sign()

if __name__ == "__main__":
    main()
