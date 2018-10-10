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

    # add block to blockchain `chain`
    def add_block(self, transactions):
      new_block = Block(transactions, self.chain[len(self.chain) - 1].hash)
      self.chain.append(new_block)
      pass


  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if current.generate_hash() != current.hash:
      	return False
      elif previous.generate_hash() != current.previous_hash:
        return False
      else:
        return True
    pass
