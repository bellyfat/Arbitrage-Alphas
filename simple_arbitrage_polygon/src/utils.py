from web3 import Web3, middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy, slow_gas_price_strategy, fast_gas_price_strategy

import abi
BSC = ['https://bsc-dataseed3.binance.org/',
		'https://bsc-dataseed.binance.org/',
		'https://bsc-dataseed1.defibit.io/',	
		'https://bsc-dataseed1.ninicoin.io',
		'https://bsc-dataseed2.defibit.io/',
		'https://bsc-dataseed3.defibit.io/',
		'https://bsc-dataseed4.defibit.io/',
		'https://bsc-dataseed2.ninicoin.io/',
		'https://bsc-dataseed3.ninicoin.io/',
		'https://bsc-dataseed4.ninicoin.io/',
		'https://bsc-dataseed1.binance.org/',
		'https://bsc-dataseed2.binance.org/',
		'https://bsc-dataseed3.binance.org/',
		'https://bsc-dataseed4.binance.org/'
		]
polygon2 = 'https://rpc-mainnet.maticvigil.com/'
polygon_rpcs =  [
	'https://rpc-mainnet.matic.network', 
	'https://matic-mainnet.chainstacklabs.com', 
	'https://rpc-mainnet.maticvigil.com', 
	'https://rpc-mainnet.matic.quiknode.pro', 
	'https://matic-mainnet-full-rpc.bwarelabs.com',
	'https://matic-mainnet-archive-rpc.bwarelabs.com',
	'https://rpc.polycat.finance/',
	'https://polygon-rpc.com',
	
]
polygon_wss = [
	'wss://rpc-mainnet.matic.network',
	'wss://ws-matic-mainnet.chainstacklabs.com',
	'wss://rpc-mainnet.maticvigil.com/ws',
	'wss://rpc-mainnet.matic.quiknode.pro',
	'wss://matic-mainnet-full-ws.bwarelabs.com',
	'wss://matic-mainnet-archive-ws.bwarelabs.com',
	'wss://polygon-rpc.com'
]

quicknode =''
quicknode_wss = ''
localNode = 'http://localhost:10545'

local = ' http://127.0.0.1:8545/'
rinkeby = ''
eth = ''


#web3 = Web3(Web3.IPCProvider('/home/ubuntu/drive/bor-data/bor.ipc',request_kwargs={'timeout': 100000})) 
web3 = Web3(Web3.HTTPProvider(polygon_rpcs[-1]))
'''web3.middleware_onion.inject(middleware.geth_poa_middleware, layer=0)
web3.middleware_onion.add(middleware.time_based_cache_middleware)
web3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
web3.middleware_onion.add(middleware.simple_cache_middleware)
'''

def factory(address):
	return web3.eth.contract(
		abi=abi.factory_abi,
		address=address
		)

def pair(address):
	return web3.eth.contract(
		abi=abi.pair_abi,
		address=address
		)

def router(address):
	return web3.eth.contract(
		abi=abi.uniswap_abi,
		address=address
		)

def archer_router():
	return web3.eth.contract(
		abi=abi.archer_router_abi,
		address='0x87535b160E251167FB7abE239d2467d1127219E4'
	)

def token(address):
	return web3.eth.contract(
		abi=abi.erc20_abi,
		address=address
		)


def get_pair_address(factory_address, token0, token1):
    return factory(factory_address).functions.getPair(token0, token1)

def get_reserves(pair_address):
    return pair(pair_address).functions.getReserves()


def router(address):
    return web3.eth.contract(abi=abi.uniswap_abi, address=address)

def get_web3(gas_price_strategy=None):
	if gas_price_strategy:
		web3.eth.set_gas_price_strategy(gas_price_strategy)
		return web3

	return web3

def get_web3_wss(timeout=60):
	return Web3(Web3.WebsocketProvider(polygon_wss[1], websocket_timeout=timeout)) 


def get_gas_price(strategy='fast'):
	if strategy == 'fast':
		r = get_web3(fast_gas_price_strategy)
		return r.eth.generate_gas_price()
		
