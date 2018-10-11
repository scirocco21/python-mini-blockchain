from blockchain import Blockchain
from hashlib import sha256

# instantiate new blockchain with genesis block
my_blockchain = Blockchain()

# add first block to the chain with argument of new_transactions
new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

# try to change the first block's transaction record with some other value
my_blockchain.chain[1].transactions = "fake_transactions"

# basic validate_chain method will return false: the current hash of the block will not equal the generated hash of the blockn (in other words, its initial correct value does not match the hash that would now be produced with the false record)
my_blockchain.validate_chain()

# a nonce ("number only used once") is a number added to a hashed block that, when rehashed, meets the difficulty level restrictions
# In this simplified example, the nonce is increased to meet a difficulty of two, where 2 refers to two leading zeros in the hash
new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0
# creating the proof
proof = sha256(str(nonce).encode() + str(new_transactions).encode()).hexdigest()
print(proof)
# finding a proof that has 2 leading zeros
while proof[:2] != '0'*difficulty:
  nonce += 1
  proof = sha256(str(nonce).encode() + str(new_transactions).encode()).hexdigest()
# the nonce value can be in the hundreds before the while loop terminates and the difficulty requirement is met
