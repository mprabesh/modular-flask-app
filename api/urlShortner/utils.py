import hashlib
import base58


def sha256_of(input_string):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode('utf-8'))

    # Return the SHA-256 hash as a bytes object
    return sha256_hash.digest()


def base58_encoded(bytes_input):
    # Encode the bytes using Base58
    encoded = base58.b58encode(bytes_input)

    # Return the Base58 encoded string
    return encoded.decode('utf-8')


# Convert the integer to a string: Use Python’s str() function.
# Encode the string to bytes: Use .encode('utf-8').
# Base58 encode the bytes: Use the base58 library.
def hash_my_url(input_string):
    try:
        sha256_result = sha256_of(input_string)
        into_integer=int.from_bytes(sha256_result, byteorder='big') % (2**64)
        finalString=str(into_integer).encode('utf-8')
        encoded=base58.b58encode(finalString).decode('utf-8')
        return encoded[:8]
    except Exception as e:
        print(f"An error occurred: {e}")
        


