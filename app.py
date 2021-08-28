from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/1919aa400e9d48438d75dfca078b55f3"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.eth.blockNumber)

