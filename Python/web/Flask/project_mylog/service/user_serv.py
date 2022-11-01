from models.user import User
import dao.user_dao as user_dao
import random
import hashlib


def getRandChar(n):
    result = []
    sample = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
    for i in range(n):
        char = random.choice(sample)
        result.append(char)
    return ''.join(result)


def get_sha1(text):
    hash_sha1 = hashlib.sha1()
    hash_sha1.update(text.encode('utf-8'))
    return hash_sha1.hexdigest()


def user_with_username_password(username: str, password: str):
    user = User
    user.username = username
    user.salt = getRandChar(16)
    user.password = get_sha1(user.salt+password)
    return user
