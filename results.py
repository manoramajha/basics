#!/usr/bin/python

import requests
import time
# Function to scrape the results from the source code 
def spider(max):
    # X is a variable which stores the hall ticket numbers
    X = 1603210001
    # text_file is the csv file where all the output is written
    text_file = open("Output3.csv",'w')
    while X <= max:
        ''' find this kind of specific url by entering the hall ticket number in any results site
            and before clicking enter click on inspect element and go to network and then click enter.
            there will be a AJAX link . that is the specific link which has all the raw data of results,
            which can be separated into different cells using delimiters in any spreadsheet application '''
        url = "http://schools9.com/andhra/2016/2ndyear/i2-gen-2016-ap.aspx?htno=" + str(X)
        # the script sleeps for 20 secs for every 2500 halltickets to avoid crashing the server
        if X % 2500 == 0:
            time.sleep(20)
            source_code = requests.get(url)
            plain_text = source_code.text
            text_file.write(plain_text)
            text_file.write('\n')
            print(plain_text)
            X += 1
        else:
             source_code = requests.get(url)
             plain_text = source_code.text
             text_file.write(plain_text)
             text_file.write('\n')
             print(plain_text)
             X += 1
    # Close the csv file. Now the csv file is saved in the home folder
    text_file.close()

spider(1603210101)

