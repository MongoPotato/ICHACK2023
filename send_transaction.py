from Transactions import Transaction
import json
import time
from BlockNode import SportNode
import signing
from hashlib import sha256
from signing import Signing


def gohash(data):
    return sha256(data).hexdigest()  


filename = "transaction.json"
ipnode = "146.179.200.156"
iphost = "146.179.195.212"
f = open(filename)

data = json.load(f)

transaction = Transaction(data['sender'], data['receiver'], data['amount'], data['date'])
node = SportNode(ipnode, 10002)
node.start()
node.connect_with_node(iphost, 10001)
time.sleep(2)
signings = Signing(transaction.getSender(), transaction.getReceiver())
signature = signings.signs(transaction)

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





