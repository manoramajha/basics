#!/usr/bin/python
import time
import requests
from bs4 import BeautifulSoup

print ('Hello Welcome to FreeFlix v0.0 Beta ')

time.sleep(0.5)
print('Make sure you have a torrent client like Bittorrent/uTorrent')
time.sleep(0.5)
print('Enter the name of the movie. Be as precise as possible. Include year of release and language to get accurate results ')
movie_name = input()
string_list = movie_name.split(" ")
url_ready = '+'.join(string_list)
final_url = ("https://kat.cr/usearch/" + url_ready + '+category%3Amovies/?field=seeders&sorder=desc')

url= final_url
source_code=requests.get(url)
plain_text= source_code.text
soup = BeautifulSoup(plain_text,"lxml")
sizes = ['0']
names = ['0']
torrent_links = ['0']


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
for n in range(1,26):

    p = str(sizes[n])
    q = str(names[n])
    r = str(n)


    print('S.no '+ r +  ' Size: ' + p + '  Name: ' + q )
time.sleep(1)
print("Enter the S.no of the file you wish to download")
x=int(input())
final_stuff = torrent_links[x]
print(final_stuff)
print('click on the above link to get the torrent file and start the download')


