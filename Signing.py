from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Signing:
    def __init__(self, public_key, private_key, transaction):
        self.public_key = public_key
        self.private_key = private_key
        self.transaction = transaction
        self.signature = self.sign()

    def sign(self):
        return self.private_key.sign(self.transaction, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

