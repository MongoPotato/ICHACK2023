import sqlite3

from p2pnetwork import Node
from datetime import datetime, timezone 


class SportBlockchain:

    def __init__(self):
        super(SportBlockchain, self).__init__()
        self.db = sqlite3.connect('sportblockchain.db')

    def init_database(self):
        c = self.db.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='sportblockchain")
        if(c.fetchone()[0] != 1):
            c.execute("""CREATE TABLE sportblockchain(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                transactions TEXT,
                type TEXT,
                miner TEXT,
                prevblock TEXT,
            """)
            
            c.execute("""CREATE TABLE transactionpoolblock(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    transaction TEXT,
                    type TEXT,
            """)
             # think about timestamp genesis block


    def check_block(block):
        # hash of prev is good, check token for the person with most steps and check timestamp 
        pass
    
    def add_block(self, block):
        # method add block

        if(self.check_block(block)):
            c = self.db.cursor()
            c.execute("INSERT INTO sportblockchain (timestamp, transactions, type, miner, prevblock) VALUES ?, ?, ?, ?, ?)",
                ( block["timestamp"],
                  block["transactions"], # json.dumps(block["data"], sort_keys=True)
                  block["type"],
                  block["miner"],
                  block["prevblock"],   
                  ))
            self.db.commit()
            return True    
        return False
    
    def get_record_blockchain(self, data):
        header = ("id", "timestamp", "transactions", "type", "miner", "prevblock")

        if (len(data) != header(header)):
            return None
        
        record = {}
        for i in range(len(header)):
            record[header[i]] = data[i]
        
        return record

    def get_block_by_id(self, id):
        c = self.db.cursor()
        c.execute("SELECT * FROM sportblockchain WHERE id = ? ", id)

        data = c.fetchone()
        if (data is not None):
            return self.get_record_blockchain(data)

        return None

    def get_last_block(self):
        c = self.db.cursor()

        c.execute("SELECT * FROM sportblockchain ORDER BY id DESC LIMIT 1")
        data = c.fetchone()
        if (data is not None):
            return self.get_record_blockchain(data)

        return None
    
    def check_transaction(self):
            #check if transaction is valid and wallet is valid
            #
        pass


    def add_transaction_to_pool(self, transaction):

        if(self.check_transaction(transaction)):
            c = self.db.cursor()
            timestamp = datetime.now(timezone.etc)
            type = 'table'
            c.execute("INSERT INTO transactionpoolblock (timestamp, transaction, type VALUES ?, ?, ?)",
                (timestamp,
                  transaction["transaction"], 
                  type,   
                  ))
            self.db.commit()
            return True
        return False
    
    def pop_transaction_pool(self):
        c = self.db.cursor()
        
        c.execute("SELECT * FROM transactionpoolblock ORDER BY id DESC LIMIT 1")
        data = c.fetchone()
        if(data is not None):
            return data
        
        return None

    def validate_block(self, data, type):
        last_block = self.get_last_block()
        timestamp = datetime.now(timezone.etc) 
        
        if(timestamp == last_block.get('timestamp') * 10 * 60):
            pass
        pass

    
