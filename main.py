import sys
import math
import requests
import json
import time
import datetime
from pandas import read_csv

# function to input an API Key
def check_api_key():
	api_key = input("Insert a valid API Key: ")
	return(api_key)

# load data from the e-mail
def load_data():
	city_id = read_csv('id_city.csv', 
				sep=',', 
				usecols=['id'], 
				squeeze=True)
	city_id = list(city_id)
	return(city_id)

base_url =	'http://api.openweathermap.org/data/2.5/weather'
city_id =	load_data()
api_key =	""

variables_per_time = 60
time_sleep = 60

# extract data from open weather web site, using its API
def data_search(city_id):
	query = base_url + '?id=%d&units=metric&APPID=%s' % (city_id, api_key)
	request = requests.get(query)
	todos = json.loads(request.content)
	data_info = {"id":todos['id'], "temp":todos['main']['temp'], "humidity":todos['main']['humidity']}
	convert_json = json.dumps(data_info)
	print(convert_json)

# print data collect
def print_info_cities():
	counter = 1
	city_id_length = len(city_id)
	for i in city_id:
		if(counter % variables_per_time != 0):
			print("ID: %d" %(counter))
			data_search(i)
			print("ID: %d" %(counter))
			print(datetime.datetime.now())
			print("Completed: %d%%" %(counter/city_id_length*100))
			counter += 1
		else:
			time.sleep(time_sleep)
			data_search(i)
			print(datetime.datetime.now())
			print("Completed: %d%%" % (counter/city_id_length*100))
			counter += 1

# function to run the program
if __name__ == '__main__':
	print_info_cities()
