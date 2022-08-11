user_name = 'odinbogus'
password = '3dZxtd5cjt'
path = '/home/fox/PycharmProjects/python_parsing/inst_bot/chromedriver'
site_path = 'https://www.instagram.com/'


if __name__ == "__main__":
    key_path = '../cr_graphy/new'
    create_key(key_path)
    # key = load_key(key_path)
    key = Fernet.generate_key()
    encrypt_file('../cr_graphy/test.txt', key)