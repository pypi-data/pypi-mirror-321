import hashlib
import time
from dataclasses import dataclass, field
import pickle
import os

@dataclass
class Block:
    """
    Represents a block in the blockchain, containing contributor reward data.
    """
    name_backtest: str  # Name of the backtest or strategy
    data: str           # Data related to the reward or contributor
    previous_hash: str = ''  # Hash of the previous block
    timestamp: float = field(default_factory=time.time)  # Timestamp of block creation
    hash: str = field(init=False)  # Automatically calculated hash

    def __post_init__(self):
        self.hash = self.calculate_hash

    @property
    def calculate_hash(self):
        """
        Calculate the hash of the block using its contents.
        """
        return hashlib.sha256(
            (str(self.timestamp)
             + self.name_backtest
             + self.data
             + self.previous_hash).encode()
        ).hexdigest()

@dataclass
class Blockchain:
    """
    Represents a blockchain for storing backtest data and rewards.
    """
    name: str  # Name of the blockchain file
    chain: list = field(default_factory=list)  # List of blocks in the blockchain

    def store(self):
        """
        Persist the blockchain to a file.
        """
        os.makedirs('blockchain', exist_ok=True)
        with open(f'blockchain/{self.name}.pkl', 'wb') as f:
            pickle.dump(self, f)

    def __post_init__(self):
        # Initialize the chain with the genesis block
        self.chain.append(self.create_genesis_block())
        self.store()

    def create_genesis_block(self):
        """
        Create the genesis block (the first block in the chain).
        """
        return Block('Genesis Block', '', '0')

    def add_block(self, name: str, data: str):
        """
        Add a new block to the blockchain.

        :param name: Name of the backtest or strategy.
        :param data: Data related to the reward or contributor.
        """
        previous_block = self.chain[-1]
        new_block = Block(name, data, previous_block.hash)
        self.chain.append(new_block)
        self.store()

    def is_valid(self):
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash is still valid
            if current_block.hash != current_block.calculate_hash:
                return False

            # Check if the current block points to the correct previous hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        """
        Display the contents of the blockchain.
        """
        to_return = ''
        for i, block in enumerate(self.chain):
            to_return += "-" * 80 + '\n'
            to_return += f"Block {i}\n"
            to_return += "-" * 80 + '\n'
            to_return += f"Backtest: {block.name_backtest}\n"
            to_return += f"Timestamp: {block.timestamp}\n"
            to_return += f"Hash: {block.hash}\n"
            to_return += f"Previous Hash: {block.previous_hash}\n"
            to_return += "-" * 80 + '\n'
        return to_return

    def remove_blockchain(self):
        """
        Delete the blockchain file.
        """
        os.remove(f'blockchain/{self.name}.pkl')

def add_reward(blockchain_name: str, name: str, reward_data: str):
    """
    Add a reward block to the blockchain.

    :param blockchain_name: Name of the blockchain file.
    :param name: Name of the contributor or strategy.
    :param reward_data: Data about the reward (e.g., amount, currency).
    """
    blockchain = load_blockchain(blockchain_name)
    blockchain.add_block(name, reward_data)
    blockchain.store()

def withdraw_reward(blockchain_name: str, contributor_name: str):
    """
    Simulate the withdrawal of rewards by displaying the contributor's rewards.

    :param blockchain_name: Name of the blockchain file.
    :param contributor_name: Name of the contributor.
    :return: List of rewards for the contributor.
    """
    blockchain = load_blockchain(blockchain_name)
    rewards = [
        block.data for block in blockchain.chain
        if block.name_backtest == contributor_name
    ]
    return rewards

def load_blockchain(name: str):
    """
    Load an existing blockchain from a file.

    :param name: Name of the blockchain file.
    :return: Loaded Blockchain object.
    """
    with open(f'blockchain/{name}.pkl', 'rb') as f:
        return pickle.load(f)

def remove_blockchain(name: str):
    """
    Delete a blockchain file.

    :param name: Name of the blockchain file.
    """
    os.remove(f'blockchain/{name}.pkl')
