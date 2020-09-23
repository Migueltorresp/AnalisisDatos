
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "LUL1OxlHJxGlPgXSbE8g9nHG0"
csecret = "0th8nNK9p2tW2DIhCoIe0SFTF3eZk2bKRH5Fh9HQy8vBVvFjeM"
atoken = "3332882014-pJ41tpRKk5KSkTpufA0u0WF3p8cbjFuAhL4j8D9"
asecret = "MajGluxKMnWtA8HXGTIwbUDa0n62GlarvOs3rzzzvQYIh"
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

server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('provincias')
except:
    db = server['provincias']
    
    
'''===============LOCATIONS=============='''    
 
twitterStream.filter(track=['Candidatos', 'Presidencia','lista presindencial','politica','diputados','partidos politicos','Politicos','asamblea nacional','elecciones 2021','postulantes','electoral'])

twitterStream.filter(locations=[-80.5634,-3.0643,-79.1019,-0.8367])
