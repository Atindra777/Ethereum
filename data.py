from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/1919aa400e9d48438d75dfca078b55f3"
web3 = Web3(Web3.HTTPProvider(infura_url))

blockNumber = web3.eth.blockNumber

#for i in range(0, 10):
#    print(web3.eth.getBlock(blockNumber - i))

hash = '0x55c9971e4ee18cd8f7366947013201d821573d6c24dbccf6efd97677c97dd537'
print(web3.eth.getTransactionByBlock(hash, 3))



