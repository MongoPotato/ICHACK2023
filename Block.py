class Block:
    def __init__(self):
        self.previous_hash = ""
        self.transactions = []
        self.miner_address = "" #address of the previous miner
        self.hash = self.calculate_hash()


    def calculate_hash(self):
        #we need to calculate the hash of the block
        #the hash is going to be the hash of the previous hash, the transactions, the previous miner address and the previous miner token
        #we need to convert the transactions to a string
        transactions_string = ""
        for transaction in self.transactions:
            transactions_string += str(transaction.sender) + str(transaction.receiver) + str(transaction.amount) + str(transaction.date) + str(transaction.signature)
        return sha256((str(self.previous_hash) + transactions_string + str(self.miner_address)).encode()).hexdigest()
