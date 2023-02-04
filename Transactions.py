import Wallet
from Signing import Signing


class Transaction:
    def __init__(self,sender,receiver,amount,date):
        self.sender = sender #identified by the public key
        self.receiver = receiver #identified by the public key
        self.amount = amount  #amount of money beign sent after commission is taken by the miner
        self.date = date 
        self.signature = self.sign()

        #database transaction -> sender, receiver, amount, 

    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getAmount(self):
        return self.amount

    def payToWallet(self):
        pass


