import random, datetime, json, web3
from web3 import contract
from web3.main import Web3

random = random.random()
random = str(random)
timestamp = datetime.datetime.now()
timestamp = str(timestamp)

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"name":"getProject","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_Random","type":"string"},{"internalType":"string","name":"_Timestamp","type":"string"}],"name":"setProject","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress('0x86cE5438E8c81382b7B8D51ad6593Bf8D4A6D78f')

contract = web3.eth.contract(address=address, abi=abi)

tx_hash = contract.functions.setProject(random, timestamp).transact()

tx_reciept = web3.eth.waitForTransactionReceipt(tx_hash)

data = contract.functions.getProject().call()

print(data)
