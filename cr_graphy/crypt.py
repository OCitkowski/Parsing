# https://www.thepythoncode.com/code/encrypt-decrypt-files-symmetric-python
from cryptography.fernet import Fernet
# Importing the os library
import os


def write_key(key_path):
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def load_key(path_key):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(path_key, "rb").read()

def encrypt(filename, key, prefix : str = 're_'):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(prefix + filename, "wb") as file:
        file.write(encrypted_data)

    with open(filename, "wb") as file:
        file.write(b'#file is crypted')



def decrypt(filename, key, prefix : str = 're_'):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(prefix + filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Encryptor Script")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-key", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    file = args.file
    generate_key = args.generate_key

    if generate_key:
        # python crypt.py ../cr_graphy/new -key
        path_key = args.file
        write_key(path_key)

    else:
        # load the key
        print('Enter path to key-')
        path_key = input()
        key = load_key(path_key)

        encrypt_ = args.encrypt
        decrypt_ = args.decrypt

        if encrypt_ and decrypt_:
            raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
        elif encrypt_:
            encrypt(file, key)
        elif decrypt_:
            decrypt(file, key)
        else:
            raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")