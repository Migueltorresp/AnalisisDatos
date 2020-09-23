#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#En este script recolecto datos y almaceno en MongoDB remoto sobre 
#Pulso político en 20ciudades principales deEcuador, listas y candidatos, presidenciales y diputados.
#---------COVID NIVEL MUNDIAL 2--------------
#nuevas API keys

###API ########################
ckey = "dmb808yiLRpIukUzlEKfsgAUk"
csecret = "7K68QsfAcxvsEwMQf8ZpHJIhETtLVMLWU0mJVjraUITLVx1ivG"
atoken = "115946548-nd0Rp8L3xKoKVT2pNZEw5XuUj8wPCljNwxp7o8P8"
asecret = "SNHrscz4GeLTzHd5FEG2AqaUZz7sqCj8LYD7yp18sZKSu"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id']) 
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''======== CouchDB'=========='''

server = couchdb.Server('http://admin:1234@localhost:5984/')  
try:
    db = server.create('covid-19')
except:
    db = server['covid-19']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['covid','covid-19','pandemia','vacuna','pandemic','cure','cura'])

