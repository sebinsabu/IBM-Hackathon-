from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
from flask import flash, redirect,session, abort
from random import randint
import atexit
import os
import json
import time
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions, EmotionOptions
from textblob import TextBlob
import tweepy
import pandas as pd
from operator import add
import re


app = Flask(__name__, static_url_path='')

db_name = 'mydb'
client = None
db = None
# namei = 'sebine'


if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000


    # Chrone job to collect big dataset of tweets.

# name = "sebinien"

port = int(os.getenv('PORT', 8000))

@app.route('/hello/<string:twid>/<string:name>')


def user_input(name,twid):
    
   
    # nameofuser = name
    
    return render_template('userinput1.html' ,name=name,twid=twid)



@app.route('/user_inputIBMapi', methods=['POST'])
def input_return():
  userfeedback = request.form['feedback']
  tweetid = request.form['tweetid']
  natural_language_understanding = NaturalLanguageUnderstandingV1(

  username='6c767224-ec65-43cb-91d3-eea204c9cc9d',
  password='o2MQGv8WIvTm',
  version='2018-03-16')

####input your credentials here
  consumer_key = 'VFBEwMpMjtlV8OIA0mfucV6kY'
  consumer_secret = 'eukgnIEVhoXF2B7Z34UpDozbNoBPza97A8eimYQKX5gVij8WKc'
  access_token = '1041578973338066944-kvBimbneKmEGrXZeUralzYQB3fY4a6'
  access_token_secret = 'F5CnUDFqldUJL20n45wy9OI3OSg63dBIBcoVQA3baZKV2'

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth,wait_on_rate_limit=True)
  
  def twitterdatafetch(userid,datei,count):
        
    runner = 0
    tweethistory = []
    sentiment_score_summer = 0



    for tweet in tweepy.Cursor(api.user_timeline, id=userid,count=5,
                               lang="en",
                               since=datei).items():
#        print (tweet.created_at, tweet.text)
        statement = re.sub(r"http\S+", "", tweet.text)

        runner = runner + 1
        tweethistory.append(statement)
        
        if runner == count:
            return(tweethistory)
            break;


  def IBM_NLP(userinput):
        
    response = natural_language_understanding.analyze(
    
    text= userinput,
    language = 'en',
    features=Features(
        emotion=EmotionOptions(
        )))
    sadness = response.result['emotion']['document']['emotion']['sadness']
    joy = response.result['emotion']['document']['emotion']['joy']
    fear = response.result['emotion']['document']['emotion']['fear']
    disgust = response.result['emotion']['document']['emotion']['disgust']
    anger = response.result['emotion']['document']['emotion']['anger']
    return(sadness,joy,fear,disgust,anger)

  def senti_metric_average(emotion_metric):
    emotion_metric_avg = []
    n = 0
    sadness = 0
    joy = 0
    fear = 0
    disgust = 0
    anger = 0

    while n < len(emotion_metric):
            sadness = sadness + emotion_metric[n][0]
            joy = joy + emotion_metric[n][1]
            fear = sadness + emotion_metric[n][2]
            disgust = sadness + emotion_metric[n][3]
            anger = sadness + emotion_metric[n][4]
            n = n+1
            

    emotion_metric_avg.append(sadness/len(emotion_metric))
    emotion_metric_avg.append(joy/len(emotion_metric))
    emotion_metric_avg.append(fear/len(emotion_metric))
    emotion_metric_avg.append(disgust/len(emotion_metric))
    emotion_metric_avg.append(anger/len(emotion_metric))
    return(emotion_metric_avg)

  if tweetid == "nil":
        tweetid = "ndtv"
        
        
  tweetdata = twitterdatafetch(tweetid,"2017-09-19",5)

  
  emotion_metric = []
  m = 0
  while m < len(tweetdata):
    #print(IBM_NLP(tweetdata[m]))
    emotion_metric.append(IBM_NLP(tweetdata[m]))
    m = m+1  

  
  user_senti_metric = IBM_NLP(userfeedback)
#   user_senti_avgmetric = senti_metric_average(user_senti_metric)
  twitter_senti_avgmetric = senti_metric_average(emotion_metric)
 
  twitter_metric_weighed = [x * 0.2 for x in twitter_senti_avgmetric]
  user_metric_weighed = [y * 0.8 for y in user_senti_metric]


  summer = list( map(add,twitter_metric_weighed , user_metric_weighed) ) 
  m = max(summer)
  index = summer.index(max(summer))

  if index == 0:
    
    return render_template('usersad.html')

  elif index == 1:
    return render_template('userhappy.html')
  
  elif index == 2:
    return render_template('userfear.html')
  elif index == 3:
    return render_template('userbored.html')
  elif index == 4:
    return render_template('userangry.html')
  else:
    return("meh")








     
#   userfeedback = request.form['password']
    #IBM Module Start from Here.



# Adding new addition here



# @app.route('/hello')
# def rooie():
#  print('Hello Sebin')




# /**
#  * Endpoint to get a JSON array of all the visitors in the database
#  * REST API example:
#  * <code>
#  * GET http://localhost:8000/api/visitors
#  * </code>
#  *
#  * Response:
#  * [ "Bob", "Jane" ]
#  * @return An array of all the visitor names
#  */
@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    user = request.json['name']
    data = {'name':user}
    if client:
        my_document = db.create_document(data)
        data['_id'] = my_document['_id']
        return jsonify(data)
    else:
        print('No database')
        return jsonify(data)

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
