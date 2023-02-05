from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
#TODO redo

class Signing:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def createdata(self, transaction):
        data = {"sender": transaction.getSender(), "receiver": transaction.getReceiver(), "amount": transaction.getAmount()}
        return data

    def signs(self, transaction):
        return self.private_key.sign(self.createdata(transaction), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

    def verify(self, transaction, signature):
        try:
            self.public_key.verify(signature, self.createdata(transaction), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
            return True
        except:
            return False
