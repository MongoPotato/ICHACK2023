import sqlite3

from p2pnetwork import Node
from datetime import datetime, timezone 


class SportBlockchain:

    def __init__(self):
        super(SportBlockchain, self).__init__()

        self.db = sqlite3.connect('sportblockchain.db')

    def init_database(self):
        c = self.db.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='sportblockchain" )
        if(c.fetchone()[0] != 1):
            c.execute("""CREATE TABLE sportblockchain(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                transactions TEXT,
                type TEXT,
                miner TEXT,
                prevblock TEXT,
            """)

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
        # implement search function
        pass

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

    def validate_block(self, data, type):
        last_block = self.get_last_block()
        timestamp = datetime.now(timezone.etc)

        pass

    
