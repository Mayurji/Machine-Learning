from tweepy import OAuthHandler
import tweepy
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

consumer_key = 'obfMNS5GWvuT18pe41CUHiO9S'
consumer_secret = 'AmpedgaQxdW2SkRF4zLzS7F4Z7XQWwGogjgy37Ag6zMnbKUuux'
access_token = '2897676907-EBF4020k7WpvccTxiZGiaNLwGFIoJd1fghpcdcy'
access_secret_token = 'JgmjzDEyB6gO4Q9iHv6pqDL7gLIgtiKuYL5y3T8QKOrju'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret_token)
list_of_sentence = []
api = tweepy.API(auth)

def twitter_sentiments(username,no_of_tweets):
    tweets = api.home_timeline(screen_name=username,count=no_of_tweets)
    token_tweet=[]
    translator = str.maketrans('', '', string.punctuation)
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        token_tweet.append([x for x in nltk.word_tokenize(j.translate(translator)) if 'http' not in x and x != "RT" and x not in stopwords.words('english')])

    for list_of_words in token_tweet:
        list_of_words = " ".join(list_of_words)
        list_of_sentence.append(list_of_words)

    sia = SentimentIntensityAnalyzer()
    negative_score = []
    neutral_score = []
    positive_score = []
    normalized_score = []
    verdict = []
    for sentence in list_of_sentence:
        print(sentence)
        ss = sia.polarity_scores(sentence)
        for k in ss:
            #print('{0}: {1}, '.format(k, ss[k]), end='')
            if k == 'neg':   
                negative_score.append(ss[k])
            elif k == 'neu':
                neutral_score.append(ss[k])
            elif k == 'pos':
                positive_score.append(ss[k])
            elif k == 'compound':
                normalized_score.append(ss[k])
                
    for n in normalized_score:
        if n < 0:
            verdict.append("Negative Tweet")
        elif n == 0:
            verdict.append("Neutral Tweet")
        elif n > 0:
            verdict.append("Positive Tweet")
    
    Tweets_Sentiments = pd.DataFrame(np.column_stack([list_of_sentence,negative_score,neutral_score,positive_score,normalized_score,verdict]),columns=["Tweet","Negative","Neutral","Positive","Normalized","Verdict"])

    return Tweets_Sentiments

twitter_sentiments('mayur_22',100)