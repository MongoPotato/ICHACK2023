import Wallet
from Signing import Signing


class Transaction:
    def __init__(self,sender,receiver,amount,date):
        self.sender = sender #identified by the public key
        self.receiver = receiver #identified by the public key
        self.amount = amount  #amount of money beign sent after commission is taken by the miner
        self.date = date 
<<<<<<< HEAD
=======
        self.signature = self.sign()
>>>>>>> 0a4eaef3814dfd4110afff25b3d43dbcfc25e366


    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getAmount(self):
        return self.amount

    def payToWallet(self):
        pass

