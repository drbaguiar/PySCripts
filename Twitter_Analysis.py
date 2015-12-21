import numpy as np
import sys
import json
import re

def load_tweets(fp):
	lst = []

	line = fp.readline()
	while len(line) is not 0:
		data = json.loads(line.strip())
		lst.append(data)
		line = fp.readline()

	return lst

def parse_tweets(tweets):
	"""
	Parses a list of tweets, splitting the ``text`` of the tweet
	into tokens based on a regular expression.
	"""
	pattern = re.compile(r'\w+')
	parsed = []
	for t in tweets:
		if 'text' not in t.keys():
			continue

		# Obtain a list of words
		words = pattern.findall(t['text'])
		parsed.append(words)

	return parsed
	
def readSentimentList(file_name):
    ifile = open(file_name, 'r')
    happy_log_probs = {}
    sad_log_probs = {}
    ifile.readline() #Ignore title row
    
    for line in ifile:
        tokens = line[:-1].split(',')
        happy_log_probs[tokens[0]] = float(tokens[1])
        sad_log_probs[tokens[0]] = float(tokens[2])

    return happy_log_probs, sad_log_probs

def classifySentiment(words, happy_log_probs, sad_log_probs):
    # Get the log-probability of each word under each sentiment
    happy_probs = [happy_log_probs[word] for word in words if word in happy_log_probs]
    sad_probs = [sad_log_probs[word] for word in words if word in sad_log_probs]

    # Sum all the log-probabilities for each sentiment to get a log-probability for the whole tweet
    tweet_happy_log_prob = np.sum(happy_probs)
    tweet_sad_log_prob = np.sum(sad_probs)

    # Calculate the probability of the tweet belonging to each sentiment
    prob_happy = np.reciprocal(np.exp(tweet_sad_log_prob - tweet_happy_log_prob) + 1)
    prob_sad = 1 - prob_happy

    return prob_happy, prob_sad

def main():
    # We load in the list of words and their log probabilities
	happy_log_probs, sad_log_probs = readSentimentList('D:/Data/twitter_sentiment_list.csv')
    # Here we have tweets which we have already tokenized (turned into an array of words)
    #tweet1 = ['I', 'love', 'holidays']
    #tweet2 = ['very', 'sad']
	tweet_file = open(sys.argv[1])
	tweets = load_tweets(tweet_file)
	tweet1 = parse_tweets(tweets)
	
    # Calculate the probabilities that the tweets are happy or sad
	tweet1_happy_prob, tweet1_sad_prob = classifySentiment(tweet1[0], happy_log_probs, sad_log_probs)
    #tweet2_happy_prob, tweet2_sad_prob = classifySentiment(tweet2, happy_log_probs, sad_log_probs)
    
	print "The probability that tweet1 (", tweet1, ") is happy is ", round(tweet1_happy_prob,4)*100, "and the probability that it is sad is ", round(tweet1_sad_prob,4)*100
    #print "The probability that tweet2 (", tweet2, ") is happy is ", round(tweet2_happy_prob,4)*100, "and the probability that it is sad is ", round(tweet2_sad_prob,4)*100

if __name__ == '__main__':
    main()
