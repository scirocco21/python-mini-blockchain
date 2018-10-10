from blockchain import Blockchain

# instantiate new blockchain with genesis block
my_blockchain = Blockchain()

# add first block to the chain with argument of new_transactions
new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

# try to change the first block's transaction record with some other value
my_blockchain.chain[1].transactions = "fake_transactions"

# basic validate_chain method will return false: the current hash of the block will not equal the generated hash of the block.
my_blockchain.validate_chain()
