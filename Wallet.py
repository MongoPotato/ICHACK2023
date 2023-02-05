class Wallet:
    def __init__(self, private_key, public_key):
        self.private_key = private_key #the id is the private key
        self.public_key = public_key #the public key is the id of the wallet to be broadcasted
        self.balance = 0

    
    def getPublicKey(self):
        return self.public_key
    
    def getToken(self):
        return self.token
    
    def getAddress(self):
        return self.address
    
