from Transactions import Transaction
import json
import time
from BlockNode import SportNode
import Signing
from hashlib import sha256


def gohash(data):
    return sha256(data).hexdigest()  


filename = "transaction.json"
ipnode = ""
iphost = ""
f = open(filename)

data = json.load(f)

transaction = Transaction(data['sender'], data['receiver'], data['amount'], data['date'])
print("hello")
node = SportNode(ipnode, 10002)
node.start()
node.connect_with_node(iphost, 10001)
time.sleep(2)

signature = Signing.sign(transaction)

message = {}
message['_transaction'] = "transaction"
message['_sender'] = transaction.getSender()
message['_receiver'] = transaction.getReceiver()
message['_amount'] = transaction.getAmount()
message['_date'] = transaction.getDate()
message['_signature'] = signature
message['_hash'] = gohash(message)

node.send_message(message)
node.stop()





