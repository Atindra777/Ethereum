#sending transactions on ethereum
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.eth.blockNumber)

#send cryptocurrency

account_1 = "0x8b14b729AFf52Ad26ADb5476b5c7e505B8230dFA"
account_2 = "0x1079D2719d61CF85AE2Cf030E4dBb00927301917"

private_key = "b67f946450cd683895e87b87c61f9c6a2819ffe9ba6460c5d58e5b84c2dd54f4"

nonce = web3.eth.getTransactionCount(account_1)
#get the nonce
#build a transaction
tx = { #dictionary
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
#sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
#get transaction hash

