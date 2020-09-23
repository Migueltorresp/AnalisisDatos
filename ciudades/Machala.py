#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#En este script recolecto datos y almaceno en CouchDB sobre 
#Pulso político en 20ciudades principales deEcuador, listas y candidatos, presidenciales y diputados.
#---------Machala--------------

###API ########################
ckey = "6Zyv4XxVypDqHDpFoHwSTrMzX"
csecret = "3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC"
atoken = "153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq"
asecret = "WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO"
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
    db = server.create('ciudades')
except:
    db = server['ciudades']
    
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['Candidatos', 'Presidencia','lista presindencial','politica','diputados','partidos politicos','Politicos','asamblea nacional','elecciones 2021','postulantes','electoral',
                           'Centro Democrático','Andrés Arauz','Sociedad Patriótica','Lucio Gutiérrez','David Norero','Ecuatoriano Unido','Gerson Almeida',
                            'Martha Villafuerte','Avanza','Isidro Romero','Sofía Merino','Libertad es Pueblo','Justicia Social','Izquierda Democrática',
                            'Xavier Hervas','Movimiento Amigo','Pachakutik','Yaku Pérez','Virna Cedeño','Gustavo Larrea','CREO','Guillermo Lasso','Alfredo Borrero',
                            'SUMA','Guillermo Celi', 'Verónica Sevilla','Construye Ecuador','Juan Fernando Velasco','Ana María Pesantes','Juntos Podemos',
                            'Paúl Carrasco', 'Frank Vargas Anda', 'Alianza PAIS','Ximena Peña','Patricio Barriga','Concertación','César Montúfar',' Julio Villacreses'
                           ])
twitterStream.filter(locations=[-80.02869,-3.354746,-79.84235,-3.190935])

