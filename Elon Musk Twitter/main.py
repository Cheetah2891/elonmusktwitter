import json
import time
import datetime
import re


#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)
#api = tweepy.API(auth)

#cursor = tweepy.Cursor(api.user_timeline, id="elonmusk", tweet_mode="extended").items(1)

#for i in cursor:
#	print(dir(i))

with open('fulldataset.json', 'r', encoding='utf-8') as jsonfile:
	data = jsonfile.read()

tweets = json.loads(data)

key_words = ["crypto", "Crypto", "currency", "Currency", "doge", "Doge", "coin", "Coin", "fiat", "Fiat"]

class Time:
	def __init__(self, years, months, days):
		self.years = years
		self.months = months
		self.days = days

	def getDays(self):
		return int(self.days)

	def getNumDays(self):
		self.months = int(self.months)
		self.years = int(self.years)
		self.days = int(self.days)

		y = self.years * 365

		if self.months == 1 or self.months == 3 or self.months == 5 or self.months == 7 or self.months == 8 or self.months == 10 or self.months == 12:
			m = self.months * 31
		elif self.months == 4 or self.months == 6 or self.months == 9 or self.months == 11:
			m = self.months * 30
		elif self.months == 2:
			m = self.months * 28

		d = self.days

		return y + m + d

class elonMuskTweets:
	def __init__(self, date, text, likes, rt, url):
		self.date = date[0:10] 
		self.time = date[11:19] 
		self.text = text
		self.keywords = False
		self.keywords_list = []
		self.likely = "Unlikely"
		self.likes = likes
		self.rt = rt
		self.url = url

	def getDate(self):
		return self.date

	def getTime(self):
		return self.time

	def getText(self):
		return self.text

	def getLikes(self):
		return self.likes

	def getKeywords(self):
		for word in key_words:
			if re.search(word, self.text):
				self.keywords = True
				self.keywords_list.append(word)

		return self.keywords_list

	def isLikely(self):
		if self.getKeywords() != []:
			self.likely = "Very likely"
			return self.likely
		else:
			return self.likely

list_of_tweets = []
for i in range(len(tweets)):
	list_of_tweets.append(elonMuskTweets(tweets[i]['created_at'], 
		tweets[i]['full_text'], 
		tweets[i]['favorite_count'], 
		tweets[i]['retweet_count'],
		tweets[i]['url']))

list_of_favs = []
for tweet in list_of_tweets:
	list_of_favs.append(tweet.getLikes())

list_of_likely_tweets = []
for tweet in list_of_tweets:
	if tweet.isLikely() == "Very likely":
		list_of_likely_tweets.append(tweet)

# Prints likely tweets:

for tweet in list_of_likely_tweets:
	print(tweet.getText())
	print(tweet.getDate())
	print(tweet.getTime())
	print(tweet.url)
	print("--------------------------")

list_of_likely_dates = []
for tweet in list_of_likely_tweets:
	list_of_likely_dates.append(tweet.getDate())

day_zero = Time(2020, 12, 20)
day_zero_num_days = day_zero.getNumDays()

list_of_likely_dates_time_objects = []
for date in list_of_likely_dates:
	if date[5] == "0":
		list_of_likely_dates_time_objects.append(Time(date[0:4], date[6], date[8:10]))
	else:
		list_of_likely_dates_time_objects.append(Time(date[0:4], date[5:7], date[8:10]))

list_of_likely_num_days = []
for date in list_of_likely_dates_time_objects:
	list_of_likely_num_days.append(date.getNumDays())

list_of_likely_num_days_as_integers = []
for num in list_of_likely_num_days:
	list_of_likely_num_days_as_integers.append(num - day_zero_num_days + 1)

#print(list_of_likely_num_days_as_integers)

# ---------------------------------------

# Finding average number of likes

list_of_num_likes = []
for tweet in list_of_likely_tweets:
	list_of_num_likes.append(tweet.getLikes())

#print(sum(list_of_num_likes)/len(list_of_num_likes))

# Finding average number of retweets

list_of_num_rt = []
for tweet in list_of_likely_tweets:
	list_of_num_rt.append(tweet.rt)

#print(sum(list_of_num_rt)/len(list_of_num_rt))

# ---------------------------------------

list_of_coin_prices_dates = ["2021-01-01", "2021-01-08", "2021-01-15", "2021-01-29", "2021-02-05", "2021-02-12", "2021-02-19", "2021-02-26", "2021-03-05", "2021-03-12", "2021-03-19", "2021-03-26", "2021-04-02", "2021-04-09", "2021-04-16", "2021-04-23", "2021-04-30", "2021-05-07", "2021-05-14", "2021-05-21", "2021-05-28", "2021-06-04", "2021-06-11", "2021-06-18", "2021-06-25", "2021-07-02", "2021-07-09", "2021-07-16", "2021-07-23", "2021-07-30", "2021-08-06", "2021-08-13", "2021-08-20", "2021-08-27", "2021-09-03", "2021-09-10", "2021-09-17", "2021-09-24", "2021-10-01", "2021-10-08", "2021-10-15", "2021-10-22", "2021-10-29", "2021-11-05", "2021-11-12", "2021-11-19", "2021-11-26", "2021-12-03", "2021-12-10", "2021-12-17", "2021-12-24"]
list_of_coin_prices_dates_time_obj = []
for date in list_of_coin_prices_dates:
	if date[5] == "0":
		list_of_coin_prices_dates_time_obj.append(Time(date[0:4], date[6], date[8:10]))
	else:
		list_of_coin_prices_dates_time_obj.append(Time(date[0:4], date[5:7], date[8:10]))

list_of_coin_prices_dates_time_obj_ints = []
for date in list_of_coin_prices_dates_time_obj:
	list_of_coin_prices_dates_time_obj_ints.append(date.getNumDays() - day_zero_num_days)

#print(list_of_coin_prices_dates_time_obj_ints)
