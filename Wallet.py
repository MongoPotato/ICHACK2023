class Wallet:
    def __init__(self):
        self.id = "" #the id is the private key
        self.public_key = "" #the public key is the id of the wallet to be broadcasted
        self.token = "" 
        self.address = "" #hash of the token API 