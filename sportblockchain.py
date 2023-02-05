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
                date TEXT,
                miner TEXT,
                prevblock TEXT
                )
            """)

            c.execute("""CREATE TABLE transaction_list(
                id INTEGER PRIMARY KEY,
                id_blockchain INTEGER REFERENCES sportblockchain(id),
                sender TEXT,
                receiver TEXT,
                amount INTEGER,
                date TEXT,
                signature TEXT
                )""")
            

             # think about timestamp genesis block


    def check_block(block):
        # hash of prev is good, check token for the person with most steps and check timestamp 
        pass
    
    def add_block(self, block):
        # method add block

        if(self.check_block(block)):
            c = self.db.cursor()
            c.execute("INSERT INTO sportblockchain (timestamp, miner, prevblock) VALUES (?, ?, ?)",
                ( block["timestamp"],
                  block["miner"],
                  block["prevblock"]  
                  ))
            self.db.commit()
            return True    
        return False
    
    def get_record_blockchain(self, data):
        #Avoir le record du bloc avec data
        header = ("id", "timestamp", "miner", "prevblock")

        if (len(data) != len(header)):
            #Si la data est vide : il ne sert à rien de retourner le record
            return None
        
        record = {}
        for i in range(len(header)):
            record[header[i]] = data[i]
        
        return record

    def get_block_by_id(self, id):
        #Avoir les informations du block d'id id
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
            c.execute("SELECT sender, receiver FROM transaction_list")
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
            c.execute("INSERT INTO transaction_list (sender, receiver, amount, date VALUES ?, ?, ?, ?)",
                (transaction.getSender(), 
                transaction.getReceiver(),
                transaction.getAmount(),
                timestamp
                ))
            self.db.commit()
            c = self.db.cursor()
            c.execute("SELECT id FROM transaction_list ORDER BY id DESC LIMIT 1")
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

    
