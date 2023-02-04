#today we'll be creating a blockchain in python
#these are going to be the following classes: block, wallet, transaction, blockVerify 


#start with the transaction class
#in a transaction, there is the sender, the receiver, the amount, the date and the signature 

from hashlib import sha256
<<<<<<< HEAD
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa



class Signing:
    def __init__(self):
        self.public_key = ""
        self.private_key = ""
        self.signature = self.sign()

    def sign(self, transaction_hash):
        return self.private_key.sign(transaction_hash, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())


=======
>>>>>>> a066d0236461f19522af6f7bb3b487049bafc4c5

class Transaction:
    def __init__(self):
        self.sender = "" #identified by the public key
        self.receiver = "" #identified by the public key
<<<<<<< HEAD
        self.amount = 0  #amount of money being sent after commission is taken by the miner
        self.date = "" 
        self.hash = self.calculate_hash()
        self.signature = self.sign()

    def sign(self):
        return Signing(self.sender, self.sender_pk).sign(self.hash)
    
    def calculate_hash(self):
        #we need to calculate the hash of the transaction
        #the hash is going to be the hash of the sender, the receiver, the amount, the date and the signature
        return sha256((str(self.sender) + str(self.receiver) + str(self.amount) + str(self.date)).encode()).hexdigest()

    def getSender(self):
        return self.sender
    def setSender(self, sender):
        self.sender = sender
    def 
    
=======
        self.amount = 0  #amount of money beign sent after commission is taken by the miner
        self.date = "" 
        self.signature = "" 
        self.date = ""
>>>>>>> a066d0236461f19522af6f7bb3b487049bafc4c5
    

class Wallet:
    def __init__(self):
<<<<<<< HEAD
        #generate a public key and a private key with cryptography library
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048,)
        self.public_key = self.private_key.public_key()
        self.balance = 0 #amount of money in the wallet
=======
        self.id = "" #the id is the private key
        self.public_key = "" #the public key is the id of the wallet to be broadcasted
        self.token = "" 
        self.address = "" #hash of the token API 
>>>>>>> a066d0236461f19522af6f7bb3b487049bafc4c5


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

class BlockVerify:
    def __init__(self):
        self.all_tokens = []
        self.block_timer = 7
        self.all_public_keys = []


#now we need to create the blockchain
#the blockchain is going to be a list of blocks
#the first block is going to be the genesis block
#the genesis block is going to be created by the creator of the blockchain

class Blockchain:
    def __init__(self):
        self.chain = [] #list of blocks
        self.all_transactions = []  #segment the transactions for every week
        self.all_tokens = []
        self.all_public_keys = []
        self.block_timer = 7 # a week
        self.create_genesis_block()
    
    def create_genesis_block(self, miner_address):
        genesis_block = Block()
        genesis_block.previous_hash = "0"
        genesis_block.transactions = []
        # genesis_block.public_key_miner = ??
        genesis_block.miner_address = miner_address #to complete with the winner
        genesis_block.hash = genesis_block.calculate_hash()
        self.chain.append(genesis_block)
        return genesis_block

    def add_block(self, transactions, miner_address):
        new_block = Block()
        new_block.previous_hash = self.chain[-1].hash
        new_block.transactions = transactions 
        new_block.miner_address = miner_address #to complete with the winner 
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
<<<<<<< HEAD
            
=======
>>>>>>> a066d0236461f19522af6f7bb3b487049bafc4c5
        return True

    def add_transaction(self, sender, receiver, amount, date, signature):
        new_transaction = Transaction()
        new_transaction.sender = sender
        new_transaction.receiver = receiver
        new_transaction.amount = amount
        new_transaction.date = date
        new_transaction.signature = signature
        self.all_transactions.append(new_transaction)
        return new_transaction

    def add_token(self, token):
        self.all_tokens.append(token)

    def add_public_key(self, public_key):
        self.all_public_keys.append(public_key)

    def get_blockchain(self):
        return self.chain

    def get_all_transactions(self):
        return self.all_transactions

    def get_all_tokens(self):
        return self.all_tokens

    def get_all_public_keys(self):
        return self.all_public_keys

    def get_block_timer(self):
        return self.block_timer

    def get_block(self, index):
        return self.chain[index]

    def get_last_block(self):
        return self.chain[len(self.chain) - 1]

    def get_blockchain_length(self):
        return len(self.chain)

    def get_all_transactions_length(self):
        return len(self.all_transactions)

    

