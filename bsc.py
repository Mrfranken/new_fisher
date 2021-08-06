# -*- coding: utf-8 -*-
"""
:author: Vince Wen
:maintainer: Vince Wen
:contact: vincewen92@gmail.com
"""
import json
from web3 import Web3

endpoint = 'https://bsc-mainnet.web3api.com/v1/31S6YF7V6BWBPN4F7M9XP5V34SUWV8VG1N'
account_str = '0x6f5b646d2945e1b1d489cc59f6468177ce0b9152'

# go to bscscan.com to find one token and copy its abi and contract address
# for example, RACA. Its contract address is "0x043b49749e0016E965600d502E2177cA2d95B3d9"
# find it under link https://bscscan.com/address/0x043b49749e0016E965600d502E2177cA2d95B3d9
contract_address = '0x74926B3d118a63F6958922d3DC05eB9C6E6E00c6'
abi_str = '[{"inputs":[{"internalType":"address","name":"_logic","type":"address"},{"internalType":"address","name":"admin_","type":"address"},{"internalType":"bytes","name":"_data","type":"bytes"}],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"admin_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"implementation_","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

abi = json.loads(abi_str)

web3 = Web3(Web3.HTTPProvider(endpoint))
is_connected = web3.isConnected()
print(is_connected)

account = Web3.toChecksumAddress(account_str)
balance = web3.eth.getBalance(account)
nonce = web3.eth.getTransactionCount(account)
print(balance / 10 ** 18)  # how many BNB this account has

gewei_num = web3.eth.gas_price / 10 ** -9  # how much gwei




# create contract
contract = web3.eth.contract(address=contract_address, abi=abi)
total_supply = contract.functions.totalSupply().call()
decimal = contract.functions.decimals().call()
symbol = contract.functions.symbol().call()
name = contract.functions.name().call()

# If my account has RACA this token, there is method to check how many token I have
# check how many tokens in one account under specific contract
token_balance = contract.functions.balanceOf(account).call() / 10 ** decimal
print('-' * 30)

# transactions
