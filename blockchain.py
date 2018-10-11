#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self):
      self.chain = []
      self.all_transactions = []
      self.genesis_block()

    def genesis_block(self):
      transactions = []
      previous_hash = "0"
      self.chain.append(Block(transactions, previous_hash))

    # prints contents of blockchain
    def print_blocks(self):
      for i in range(len(self.chain)):
        current_block = self.chain[i]
        print("Block {} {}".format(i, current_block))
        current_block.print_contents()

    # add block to chain and return proof of work
    def add_block(self, transactions):
      previous_hash = (self.chain[len(self.chain)-1]).hash
      new_block = Block(transactions, previous_hash)
      new_block.generate_hash()
      proof = self.proof_of_work(new_block, 3)
      self.chain.append(new_block)
      return proof, new_block

      # add basic valdiations
    def validate_chain(self):
      for i in range(1, len(self.chain)):
        current = self.chain[i]
        previous = self.chain[i-1]
        # 1. if current block has been tampered with, the stored value of its hash will not equal the hash it generates based on its transations and other properties
      if current.generate_hash() != current.hash:
      	return False
        # 2. If the block is discontinuous with the chain, the chain is invalid also
      elif previous.generate_hash() != current.previous_hash:
        return False
      else:
        return True
    pass

    # basic proof of work method
    def proof_of_work(self,block, difficulty=2):
      proof = block.generate_hash()
      while proof[:difficulty] != '0'*difficulty:
        block.nonce += 1
        proof = block.generate_hash()
       block.nonce = 0
      return proof
