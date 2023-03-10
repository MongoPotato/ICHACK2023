from p2pnetwork.node import Node
from datetime import datetime, timezone 
from hashlib import sha256
from utils import verify
from sportblockchain import SportBlockchain
from Transactions import Transaction


class SportNode(Node):

    def __init__(self, host, port):
        super(SportNode, self).__init__(host, port, None)
        
        self.sportblockchain = SportBlockchain()

    def create_new_connection(self, connection, id, host, port):
        return Node(self, connection, id, host, port)

    def node_message(self, node, data):

        if self.check_message(data):
            if("_type" in data):
                if (data["_type"] == "transaction"):

                    trans = Transaction(data["_sender"], data["_receiver"], data["_amount"], data["_date"])
                    self.sportblockchain.add_transaction_to_pool(trans)
                else:
                    self.debug.print("message type unknown ", data)

    def gohash(self, data):
        return sha256(data).hexdigest()   

    def check_message(self, data):
        self.debug_print("Incomming message")
        self.debug_print(data)

        sender = data['_sender']
        receiver = data['_receiver']
        amount = data['_amount']
        date = data['_date']
        signature = data['_signature']
        data_hash = data['_hash']
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        del data['_hash']
        
        checksig = verify(sender, signature, transaction)

        checkhash = (self.gohash(data) == data_hash)

        newdata = {}
        newdata['_signature'] = signature
        newdata['_sender'] = sender
        newdata['_receiver'] = receiver
        newdata['_amount'] = amount
        newdata['_date'] = date

        return checksig and checkhash

    def create_message(self, data):

        try:
            data["_timestamp"] = datetime.now(timezone.etc) 
            data["_hash"] = self.gohash(data)
        
        except Exception as e:
            self.debug_print("Failed to create message", e.__cause__())
        return data
            
    
    def send_message(self, message):
        self.send_to_nodes(self.create_message({"_type": "transaction", "message": message}))

    def pooling_check_new_node(self):
        return self.sportblockchain.validate_block()
    
    def getBlockChain(self):
        return self.sportblockchain.get_Blockchain()
    
    def getAmountInWallet(self, pubkey):
        return self.sportblockchain.get_sum_in_wallet(pubkey)

    def getTransactionInBlock(self, id):
        return self.sportblockchain.get_Transactions(id)
    
   