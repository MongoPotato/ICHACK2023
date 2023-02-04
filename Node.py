from p2pnetwork.node import Node

class  SportNode(Node):

    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(Node, self).__init__(host, port, id, callback, max_connections)

    def create_new_connection(self, connection, id, host, port):
        return Node(self, connection, id, host, port)

    def node_message(self, node, data):
        
        pass

    def check_message(self, data):
        self.debug_print("Incomming message")
        self.debug_print(data)

        transaction = data['_transaction']
        sender = data['_sender']
        receiver = data['_receiver']
        amount = data['_amount']
        date = data['_date']
        signature = data['_signature']
        data_hash = data['_hash']

        # check signature

        # check hash

        newdata = {}
        newdata['_signature'] = signature
        newdata['_sender'] = sender
        newdata['_receiver'] = receiver
        newdata['_amount'] = amount
        newdata['_date'] = date

        
        return 