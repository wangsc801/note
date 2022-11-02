from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA1
import time


def code():
    secrets = b'my_totp_cryptography'
    totp = TOTP(secrets, 8, SHA1(), 30)
    time_value = time.time()
    totp_value = totp.generate(time_value)
    print(totp.verify(totp_value, time_value))
    print(totp_value)

code()
