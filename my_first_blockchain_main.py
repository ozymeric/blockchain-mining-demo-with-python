import random
import hashlib
import datetime
import time

class Blockchain:

    def __init__(self):
        self.chain = []
        self.nonce = 0
        self.hash = 0
        self.genesis = {
            "#": 0,
            "time_stamp": datetime.datetime.now().strftime("%c"),
            "nonce": 0,
            "previous_hash": 0,
            "hash": 0
        }
        self.chain.append(self.genesis)

    def create_new_block(self):
        a = self.chain[len(self.chain)-1]["#"]
        a += 1
        c = self.chain[len(self.chain) - 1]["hash"]
        self.mine_block()
        d = self.hash
        b = self.nonce
        q = datetime.datetime.now().strftime("%c")
        new_block = {
            "#": a,
            "time_stamp": q,
            "nonce": b,
            "previous_hash": c,
            "hash": d
        }
        self.chain.append(dict(new_block))


    def mine_block(self):
        nonce = 0
        success = False
        while not success:
            new_hash = hashlib.sha256(str(self.chain[-1]["#"]).encode() +
                                      str(self.chain[-1]["time_stamp"]).encode() +
                                      str(nonce).encode() +
                                      str(self.chain[-1]["previous_hash"]).encode()
                                      ).hexdigest()
            if new_hash[:5] == "00000":
                success = True
                self.nonce = nonce
                self.hash = new_hash
            else:
                int(nonce)
                nonce += 1



    def get_blocks(self):
        for i in self.chain:
            print(f"""
            block #: {i['#']}
            time_stamp: {i['time_stamp']}
            nonce: {i['nonce']}
            prev_hash: {i['previous_hash']}
            hash: {i['hash']}
            """)


chain = Blockchain()

chain.get_blocks()
print("\n")
#time.sleep(7)
chain.create_new_block()
print("\n")
chain.get_blocks()
print("\n")
#time.sleep(8)
chain.create_new_block()
print("\n")
chain.get_blocks()
print("\n")
#time.sleep(3)
chain.create_new_block()
print("\n")
chain.get_blocks()
print("\n")
#time.sleep(9)
chain.create_new_block()
print("\n")
chain.get_blocks()
print("\n")
#time.sleep(6)
chain.create_new_block()
print("\n")
chain.get_blocks()
print("\n")
#time.sleep(7)
chain.create_new_block()
print("\n")
chain.get_blocks()