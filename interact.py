import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = web3.toChecksumAddress('0x98e416AFD240b57EFE49cC0c86C522127003A39B')

contract = web3.eth.contract(address=address, abi=abi) #instantiate the contract
print(contract.functions.greet().call()) #reading data from smart contract functions

tx_hash = contract.functions.setGreeting('New Greeting!').transact()
print(tx_hash)

web3.eth.waitForTransactionReceipt(tx_hash)

print('Updated greeting {}'.format(
    contract.functions.greet().call()
))
