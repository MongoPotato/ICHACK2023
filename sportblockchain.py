import sqlite3

from p2pnetwork.node import Node
from datetime import datetime, timezone 
from Transactions import Transaction
from terra_modules import *

#TODO finish off win condition 


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
                type TEXT)
            """)

            c.execute("""CREATE TABLE transaction_list(
                id INTEGER PRIMARY KEY,
                id_blockchain INTEGER REFERENCES sportblockchain(id),
                sender TEXT,
                receiver TEXT,
                amount INTEGER,
                date TEXT,
                type TEXT,
                )""")
            

             # think about timestamp genesis block


    def check_block(self, block):
        c = self.db.cursor()
        c.execute("SELECT id FROM sportblockchain ORDER BY id DESC LIMIT 1")
        data = c.fetchone()
        if(data == block["prevblock"]):
            s = "op1"
            return s
        elif(data is None):
            s = "op2"
            return s
        else:
            s = "op3"
            return s
 
    
    def add_block(self, block):
        s = self.check_block(block) 
        if(s == "op1"):
            c = self.db.cursor()
            c.execute("INSERT INTO sportblockchain (timestamp, miner, prevblock) VALUES (?, ?, ?, ?)",
                (block["timestamp"],
                  block["miner"],
                  block["prevblock"],
                  'table'
                  ))

            self.db.commit()
            return True
        elif(s == "op2"):
            c = self.db.cursor()
            c.execute("INSERT INTO sportblockchain (timestamp, miner, prevblock) VALUES (?, ?, ?, ?)",
                (block["timestamp"],
                  block["miner"],
                  0,
                  'table'
                  ))

            self.db.commit()
            return True
        else:

            return False

    def add_miner_transaction(self, transaction):
        #add miner transaction for the block and the rest of transaction in cache

        c = self.db.cursor()
        c.execute("SELECT id FROM sportblockchain ORDER BY id DESC LIMIT 1")
        data = c.fetchone()
        c.execute("INSERT INTO transaction_list(id_blockchain, sender, receiver, amount, date, type) VALUES (?, ?, ?, ?, ?, ?)",
            (
             data,
             "none",
             transaction.getReceiver(),
             transaction.getAmount(),
             transaction.getDate(),
            'table',
            ))
        self.db.commit()



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
    
    def get_Blockchain(self):
        c = self.db.cursor()

        c.execute("SELECT id, date, miner, prevblock FROM sportblockchain ORDER BY DESC")
        data = c.fetchall()
        return data

    def get_Transactions(self, block_id):
        c = self.db.cursor()

        c.execute("SELECT id, id_blockchain, sender, receiver, amount, date FROM transaction_list WHERE id_blockchain = ?", block_id)
        data = c.fetchall()
        return data

    def check_transaction(self, transaction):
        c = self.db.cursor()
        
        c.execute("SELECT sender, receiver, date FROM transaction_list ORDER BY date DESC")
            
        data = c.fetchall()
        tempdatercv = None
        tempdatesend = None
        for i in data:
            if i[0] == transaction.getReceiver():
                tempdatercv = i[2]
                break
        for j in data:
            if j[0] == transaction.getSender():
                tempdatesend = j[1]
                break
        if (tempdatesend is not None and tempdatercv is not None): 

            if(tempdatercv > tempdatesend):
                c.execute("SELECT amount FROM transaction_list WHERE tempdatercv = ?", tempdatercv)
                amount = c.fetchone()
                return amount
            elif(tempdatesend > tempdatercv):
                c.execute("SELECT amount FROM transaction_list WHERE tempdatercv = ?", tempdatercv)
                amountrcv = c.fetchone()
                c.execute("SELECT amount FROM transaction_list WHERE tempdatercv = ?", tempdatesend)
                amountsnd = c.fetchone()
                amount = amountrcv - amountsnd
                return amount
            else:
                amount = -1
                return amount
            
    def get_sum_in_wallet(self, send_adr):
        transaction = Transaction(send_adr, None, None, None)
        
        amount = self.check_transaction(transaction)
        if(amount == -1):
            return 0
        return amount

    def add_transaction_to_pool(self, transaction):
        
        data = self.check_transaction(transaction)

        if(data > -1):
            c = self.db.cursor()
            timestamp = datetime.now(timezone.etc) # timing attack can post 2 transaction at the same time so wrong id
            c.execute("INSERT INTO transaction_list (sender, receiver, amount, date VALUES ?, ?, ?, ?)",
                (
                None,
                transaction.getSender(), 
                transaction.getReceiver(),
                transaction.getAmount(),
                timestamp,
                'table',
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

    def validate_block(self):
        last_block = self.get_last_block()
        timestamp = datetime.now(timezone.etc) 
        
        if(timestamp == last_block.get('timestamp') * 10 * 60):
            users = get_users()
            max_steps = 0
            argmaxsteps = None
            for user_id, reference_id in users :
                s = get_steps(user_id,(last_block.get('timestamp')-1) * 10 * 60 , last_block.get('timestamp')*10 *60)
                if s > max_steps :
                    max_steps = s
                    argmaxsteps = reference_id
            data = "WINNER API CALL"
            self.add_block(data)
            amount = 5
            transaction = Transaction(None, data["miner"], amount, timestamp) 
            self.add_miner_transaction(transaction)
        

    