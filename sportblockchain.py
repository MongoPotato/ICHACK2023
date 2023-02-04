import sqlite3

from p2pnetwork import Node
from datetime import datetime, timezone 
import Transactions

class SportBlockchain:

    def __init__(self):
        super(SportBlockchain, self).__init__()
        self.db = sqlite3.connect('sportblockchain.db')

    def init_database(self):
        c = self.db.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='sportblockchain'")
        
        if(c.fetchone()[0] != 1):
            c.execute("""CREATE TABLE sportblockchain(
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                transactions TEXT,
                type TEXT,
                miner TEXT,
                prevblock TEXT,
                )
            """)

            c.execute("""CREATE TABLE transaction_block(
                id INTEGER PRIMARY KEY,
                sender TEXT,
                receiver TEXT,
                amount INTEGER,
                date TEXT,
                type TEXT
                )""")
            
            c.execute("""CREATE TABLE transactionpoolblock(
                id INTEGER PRIMARY KEY,
                timestamp TEXT,
                type TEXT,
                transaction_id INT,
                FOREIGN KEY (transaction_id) REFERENCES transaction_block(id)
                )
            """)

             # think about timestamp genesis block


    def check_block(block):
        # hash of prev is good, check token for the person with most steps and check timestamp 
        pass
    
    def add_block(self, block):
        # method add block

        if(self.check_block(block)):
            c = self.db.cursor()
            c.execute("INSERT INTO sportblockchain (timestamp, transactions, type, miner, prevblock) VALUES (?, ?, ?, ?, ?)",
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
    
    def check_transaction(self, transaction):
        #check if transaction is valid and wallet is valid
        c = self.db.cursor()
    
        sender = transaction.getSender()
        c.execute("SELECT * FROM sportblockchain WHERE miner = ?", sender)
        data = c.fetchone()
        if(data is not None): #Si le mineur est bien présent sur la bc, on 
                # find sum on blockchain from prev transaction to check if balance is correct
            pass
        else:
            c.execute("SELECT sender, receiver FROM transaction_block")
            data = c.fetchall()
            # data check if sender or receiver from blockchain is present in transaction
            # if not reject transaction

        c.execute("SELECT transaction_block FROM transactionpoolblock")
        data = c.fetchall()

        pass


    def add_transaction_to_pool(self, transaction):

        if(self.check_transaction(transaction)):
            c = self.db.cursor()
            timestamp = datetime.now(timezone.etc) # timing attack can post 2 transaction at the same time so wrong id
            type = 'table'
            c.execute("INSERT INTO transaction (sender, receiver, amount, date VALUES ?, ?, ?, ?)",
                (transaction.getSender(), 
                transaction.getReceiver(),
                transaction.getAmount(),
                timestamp
                ))
            self.db.commit()
            c = self.db.cursor()
            c.execute("SELECT id FROM transaction ORDER BY id DESC LIMIT 1")
            transaction_id = c.fetchone()
            c.execute("INSERT INTO transactionpoolblock (timestamp, transaction_id, type VALUES ?, ?, ?)",
                (timestamp,
                  transaction_id,
                  type   
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

    
