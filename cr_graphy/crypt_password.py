# https://www.thepythoncode.com/code/encrypt-decrypt-files-symmetric-python
import os

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import secrets
import base64
import getpass


def generate_salt(size=16):
    """Generate the salt used for key derivation,
    `size` is the length of the salt to generate"""
    return secrets.token_bytes(size)


def derive_key(salt, password):
    """Derive the key from the `password` using the passed `salt`"""
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())


def load_salt():
    # load salt from salt.salt file
    return open("salt.salt", "rb").read()


def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """
    Generates a key from a `password` and the salt.
    If `load_existing_salt` is True, it'll load the salt from a file
    in the current directory called "salt.salt".
    If `save_salt` is True, then it will generate a new salt
    and save it to "salt.salt"
    """
    if load_existing_salt:
        # load existing salt
        salt = load_salt()
    elif save_salt:
        # generate new salt and save it
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    # generate the key from the salt and the password
    derived_key = derive_key(salt, password)
    # encode it using Base 64 and return it
    return base64.urlsafe_b64encode(derived_key)


def encrypt(filename, key):
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
    with open(filename, "w") as file:
        file.write(encrypted_data)

def encrypt_in(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write in file
    """
    f = Fernet(key)

    with open(filename, "rt") as file:
        encrypted_data =''
        lines = file.readlines()
        for line in lines:
            copy_l = line.replace('\n', '')
            l_line = line.replace(' ', '').split('=')
            line = f'{l_line[0]} = {(f.encrypt(copy_l.encode("utf-8"))).decode()}'

            encrypted_data = encrypted_data + line + '\n'

    with open(filename, "w") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted successfully")

def decrypt_in(filename, key):
    f = Fernet(key)
    with open(filename, "rt") as file:
        # read the encrypted data
        lines = file.readlines()
    # decrypt data
    try:
        decrypt_data = ''
        for line in lines:
            l_line = line.split(' = ')
            b_line = bytes(l_line[1].replace('\\n', ''),'UTF-8')
            line = f.decrypt(b_line).decode()
            decrypt_data = decrypt_data + line + "\n"
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return
    # write the original file
    with open(filename, "w") as file:
        file.write(decrypt_data)
    print("File decrypted successfully")



def encrypt_in_file(full_file_name):
    password = input('Enter your password -')
    result = False

    if not os.path.isfile("salt.salt"):
        key = generate_key(password, salt_size=16, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)

    encrypt_in(full_file_name, key)

    return result

def decrypt_in_file(full_file_name):
    password = input('Enter your password -')
    result = False

    if not os.path.isfile("salt.salt"):
        print('Don`t have salt!!!')
    else:
        key = generate_key(password, load_existing_salt=True)

    decrypt_in(full_file_name, key)

    return result



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="File Encryptor Script with a Password")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-s", "--salt-size", help="If this is set, a new salt with the passed size is generated",
                        type=int)
    parser.add_argument("-e", "--encrypt", action="store_true",
                        help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true",
                        help="Whether to decrypt the file, only -e or -d can be specified.")

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass("Enter the password for encryption: ")
    elif args.decrypt:
        password = getpass.getpass("Enter the password you used for encryption: ")

    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)

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
