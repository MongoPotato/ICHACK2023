import Wallet

class Transaction:
    def __init__(self):
        self.sender = "" #identified by the public key
        self.receiver = "" #identified by the public key
        self.amount = 0  #amount of money beign sent after commission is taken by the miner
        self.date = "" 
        self.signature = "" 

        #database transaction -> sender, receiver, amount, 

    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getAmount(self):
        return self.amount

    def payToWallet(self):
        pass

