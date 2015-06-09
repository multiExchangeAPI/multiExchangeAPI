#!/usr/bin/python3

# usage : multAPI.py exchangeName symbolPair queryType jsonQueryParams 
# pairs should be specified in lowercase with an underscore separator
#
# example : multAPI.py btce btc_usd trade [{'type':'buy','price':224,'amount':0.5}]
# example : multAPI.py okcoin btc_usd orderHistory [{'since':27201}]
import sys
import json

#thisPwd = sys.pwd
#print "pwd : ",thisPwd
sys.path.insert(0, './exchanges/okcoin/rest/python')
#print 'syspath : ',sys.path
import OkcoinSpotAPI
from OkcoinSpotAPI import OKCoinSpot
#from OkcoinFutureAPI import OKCoinFuture


# see example_secrets.py, create a secrets.py based on it.
import secrets

okcoinRESTURL = 'www.okcoin.com'


if(len(sys.argv[1:])<3):
  print("not enough parameters were specified, ",len(sys.argv[1:])," specified, at least 3 needed")
  print("usage : multAPI.py exchangeName symbolPair queryType jsonQueryParams")
  exit(0)

############################# orderHistory #################################
# input params : since (integer), filled (int 0 or 1), maxListings (may be capped per exchange)
# output format :
    
if(sys.argv[3]=='orderHistory'):
  since = 0
  filled = 0
  maxListings = 0    
  if(sys.argv[1] == 'okcoin'):   
    okcoinSpot = OKCoinSpot(okcoinRESTURL,secrets.okCoinKey,secrets.okCoinSecret)
    for i in range(len(sys.argv[4:])):
      j = sys.argv[4+i].strip("'<>()[]{}").replace('\'', '\"').split(":");        
      if(j[0]=="since"):
        since = j[1]
      if(j[0]=="filled"): 
        filled = j[1]
      if(j[0]=="maxListings"):
        maxListings = j[1]        
    print("querying okcoin for orderHistory on pair ",sys.argv[2]," : since (",since,"), filled (",filled,"), maxListings (",maxListings,")")
    print (okcoinSpot.orderHistory(sys.argv[2],filled,since,maxListings))

############################# trades #################################
# input params : since (integer, refers to 'tid' or timestamp depending on exchange)
# output format :    
    
elif(sys.argv[3]=='trades'):
  since = 0
  if(sys.argv[1] == 'okcoin'): 
    okcoinSpot = OKCoinSpot(okcoinRESTURL,secrets.okCoinKey,secrets.okCoinSecret)      
    for i in range(len(sys.argv[4:])):
      j = sys.argv[4+i].strip("'<>()[]{}").replace('\'', '\"').split(":");
      if(j[0]=="since"):
        since = j[1] 
    print("querying okcoin for trades on pair ",sys.argv[2]," : since (",since,")")
    print (okcoinSpot.trades(sys.argv[2],since))       
    
    
else :
  print("queryType not recognized : ",sys.argv[3])
  print("usage : multAPI.py exchangeName symbolPair queryType jsonQueryParams")
  

#print (okcoinSpot.orderHistory('ltc_usd','0','1','2')) 
#print (okcoinSpot.trades('btc_usd','27201'))
# first page of 200 filled results (max 1 week history for okCoin)



