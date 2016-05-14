#!/usr/bin/python
import time
import requests
from bs4 import BeautifulSoup
import urllib.request

print ('Hello Welcome to FreeFlix v0.0 Beta ')

time.sleep(0.5)
print('\nMake sure you have a torrent client like Bittorrent/uTorrent')

time.sleep(0.5)
print('\nEnter the name of the movie. Be as precise as possible. Include year of release and language to get accurate results ')

movie_name = input()
full_name = str(movie_name) + ".torrent"
#breaking down the string the user entered to make it url-ready

string_list = movie_name.split(" ")
url_ready = '+'.join(string_list)
final_url = ("https://kat.cr/usearch/" + url_ready + '+category%3Amovies/?field=seeders&sorder=desc')

#scrapping the url and using bs4 to scrape by tags
source_code=requests.get(final_url)
plain_text= source_code.text
soup = BeautifulSoup(plain_text,"lxml")

#creating lists to store all the names , sizes and links of all the results
sizes = ['0']
names = ['0']
torrent_links = ['0']

#scrapping the details of results and appending them to results
for link in soup.findAll('td',{'class': "nobr center"}):
    size = link.text
    sizes.append(size)

for links in soup.findAll('a',{'class': "cellMainLink"}):
    name = links.string
    names.append(name)

for linkss in soup.findAll('a', {'title': "Download torrent file"}):
    href = linkss.get("href")
    lunks = 'https:' + href
    torrent_links.append(lunks)
print('Files are arranged from descending order of no. of seeds ')
for n in range(1,11):
    # converting all the data into strings to make sure it is easy to add them to display the reults
    p = str(sizes[n])
    q = str(names[n])
    r = str(n)


    print('S.no '+ r +  ' Size: ' + p + '  Name: ' + q )
time.sleep(0.5)

print("Enter the S.no of the file you wish to download")

# asking user to choose the best suited file
x=int(input())
final_stuff = torrent_links[x]

# takes the user input . copies the url of torrent file

opener = urllib.request.build_opener()

# add headers so that the site can't detect the crawler

opener.addheaders = [('User-Agent', 'CERN-LineMode/2.15 libwww/2.17b3')]

urllib.request.install_opener(opener)  # NOTE: global for the process

urllib.request.urlretrieve(final_stuff, full_name)

