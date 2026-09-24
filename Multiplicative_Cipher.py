# ============================================================
# Multiplicative Cipher
# Encryption and Decryption
# No External Dependencies
# ============================================================

ALPHABET_SIZE = 26


# ------------------------------------------------------------
# Find GCD
# ------------------------------------------------------------

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# ------------------------------------------------------------
# Find Modular Inverse
# ------------------------------------------------------------

def mod_inverse(key):

    for i in range(1, ALPHABET_SIZE):

        if (key * i) % ALPHABET_SIZE == 1:
            return i

    return None


# ------------------------------------------------------------
# Encryption
# Formula:
# C = (P × K) mod 26
# ------------------------------------------------------------

def encrypt(text, key):

    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                p = ord(char) - ord('A')

                c = (p * key) % ALPHABET_SIZE

                result += chr(c + ord('A'))

            else:
                p = ord(char) - ord('a')

                c = (p * key) % ALPHABET_SIZE

                result += chr(c + ord('a'))

        else:
            # Keep spaces, numbers and symbols unchanged
            result += char

    return result


# ------------------------------------------------------------
# Decryption
# Formula:
# P = (C × K^-1) mod 26
# ------------------------------------------------------------

def decrypt(text, inverse_key):

    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():

                c = ord(char) - ord('A')

                p = (c * inverse_key) % ALPHABET_SIZE

                result += chr(p + ord('A'))

            else:

                c = ord(char) - ord('a')

                p = (c * inverse_key) % ALPHABET_SIZE

                result += chr(p + ord('a'))

        else:

            result += char

    return result


# ============================================================
# MAIN PROGRAM
# ============================================================

print("========================================")
print("       MULTIPLICATIVE CIPHER")
print("========================================")

plaintext = input("Enter plaintext: ")

key = int(input("Enter multiplicative key: "))


# ------------------------------------------------------------
# Validate key
# ------------------------------------------------------------

if key < 0 or key >= 26:

    print("\nError: Key must be between 0 and 25.")

    exit()


# Key must be coprime with 26

if gcd(key, 26) != 1:

    print("\nError: Invalid key.")

    print("Key must be relatively prime to 26.")

    print("Valid keys are:")

    valid_keys = []

    for i in range(1, 26):

        if gcd(i, 26) == 1:
            valid_keys.append(i)

    print(valid_keys)

    exit()


# ------------------------------------------------------------
# Calculate Modular Inverse
# ------------------------------------------------------------

inverse_key = mod_inverse(key)


# ------------------------------------------------------------
# Encryption
# ------------------------------------------------------------

ciphertext = encrypt(
    plaintext,
    key
)


# ------------------------------------------------------------
# Decryption
# ------------------------------------------------------------

decrypted_text = decrypt(
    ciphertext,
    inverse_key
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n========================================")
print("                 RESULT")
print("========================================")

print("\nPlaintext:")
print(plaintext)

print("\nEncryption Key:")
print(key)

print("\nFormula:")
print("C = (P × K) mod 26")

print("\nMultiplicative Inverse:")
print(inverse_key)

print("\nDecryption Formula:")
print("P = (C × K⁻¹) mod 26")

print("\nEncrypted Text:")
print(ciphertext)

print("\nDecrypted Text:")
print(decrypted_text)

print("\n========================================")
print("          PROGRAM COMPLETED")
print("========================================")
