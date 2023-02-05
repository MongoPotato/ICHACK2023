from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import cryptography.hazmat.primitives.serialization as sz

class Signing:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def createdata(self, transaction):
        data = {"sender": transaction.getSender(), "receiver": transaction.getReceiver(), "amount": transaction.getAmount()}
        return data

    def signs(self, transaction):
        privkey = sz.load_pem_private_key(self.private_key,password = None)
        return privkey.sign(self.createdata(transaction), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    def verify(self, transaction, signature):
        try:
            pubkey = sz.load_pem_public_key(self.public_key)
            pubkey.verify(signature, self.createdata(transaction), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
            return True
        except:
            return False
