from web3 import Web3
from decimal import Decimal
import time
while True:
 bsc = "https://bsc-dataseed.binance.org/"
 web3 = Web3(Web3.HTTPProvider(bsc))
 print(web3.isConnected())
  
 account_1 = "0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3"
 account_2 = "0x136732f39b63A29b7b0a575A0B0bBDDC602325fC"
 #private_key = "0xee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258"

 balance = web3.eth.get_balance(account_1)
 humanReadable = web3.fromWei(balance,"ether")
 print(humanReadable)
 max_transfer=humanReadable-Decimal(0.000105)
 print(max_transfer)

 #nonce = web3.eth.getTransactionCount(account_1)
if max_transfer>0:
 tx = {
     'nonce':web3.eth.getTransactionCount(account_1),
     'to':account_2,
     'value':web3.toWei(max_transfer,'ether'),
     'gas':21000,
     'gasPrice':web3.toWei('50','gwei')
 }
 try:
      signed_tx = web3.eth.account.signTransaction(tx, 0xee9cec01ff03c0adea731d7c5a84f7b412bfd062b9ff35126520b3eb3d5ff258)
      tx_Hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
      trans = web3.toHex(tx_Hash)


      transaction = web3.eth.get_transaction(trans)
      print(transaction) 
 except:
      time.sleep(3)