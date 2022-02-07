#!/usr/bin/python3
# coding: utf-8

from bs4 import BeautifulSoup # for parsing requests content and extract musics links
import requests # for fetching requests to sites
import urllib # for finding duplicat musics with their size
from urllib.parse import unquote # for decoding url to simple text
import os # for creating folder
import sys
import platform
import time
import pyfiglet
from tqdm import tqdm # for showing download progress bar
from random import randint # for making duplicate folder

plt = platform.system()

if plt == "Windows":
    pla = '\\'
elif plt == "Linux":
    pla = '/'

print('#'*60)
print(pyfiglet.figlet_format('Music Downloader', font='slant'))
print('Made by Ali Hosseinverdi')
print('#'*60)

signer_name = input("\nEnter signer name: ") # taking the name of signer

sys.stdout.write('\nSearching .../')
sys.stdout.flush()

total_links = [] # output of get_links func will append here(for comparing with site has more musics)

def get_links(url): # getting musics links
    url += signer_name.replace(" ", "-").replace("ي", "ی")
    site = requests.get(url)
    text = site.text

    try:
        bs = BeautifulSoup(text, "html.parser")
        links = bs.find_all("audio") # finding audio tags from response
        links = [i["src"] for i in links] # getting links from audio tags

        url += "/page/"

        for i in range(2,99): # getting links from next pages
            if i % 2 == 0:
                sys.stdout.write('\033[D\\')
                sys.stdout.flush()
            else:
                sys.stdout.write('\033[D/')
                sys.stdout.flush()

            url_next_page = url + str(i)
            site = requests.get(url_next_page)
            if site.status_code == 200:
                text = site.text
                bs = BeautifulSoup(text, "html.parser")
                links_next_page = bs.find_all("audio")
                [links.append(j["src"]) for j in links_next_page]
            else:
                break

       # sizes = []

       # for i in range(len(links)): # removing same size(MB) links(Because some of musics may uploaded twice in site)
       #     try:
       #         url = links[i]
       #     except IndexError:
       #         break
       #     try:
       #         size = urllib.request.urlopen(url)
       #     except urllib.error.HTTPError:
       #         break
       #     except UnicodeEncodeError:
       #         break
       #     length = size.length
       #     sizes.append(length)
       #     num = sizes.count(length)
       #     if num == 2:
       #         b = links[i]
       #         links.remove(b)

	 	
        total_links.append(links)
    except:
        total_links.append([""])
        

# finding musics links from sites
get_links("https://upmusics.com/tag/")
get_links("https://music-fa.com/artist/")


# find wich site has more musics from this signer
if len(total_links[0]) > len(total_links[1]):
    links = total_links[0]
else:
    links = total_links[1]

os.system("clear")

if len(links) == 0:
    print("Signer not found !!!")
    quit()
else:
    print(f"There are {len(links)} musics from this signer") # printing the number of musics to user
    how_many_user_download = int(input("How many musics you want to download?: ")) # get the number of musics that user want to download

print("\n")

if how_many_user_download == 0:
    quit()

try: # creating directory for downloading musics in there
    os.mkdir(signer_name)
except FileExistsError:
    signer_name = signer_name + str(randint(1,9999))
    os.mkdir(signer_name)

for i in range(0,how_many_user_download): # downloading musics
    music_name = unquote(links[i].split("/")[-1]) # getting the name of song
    music_name = music_name.split("-")[-1].replace("128", "").replace(")", "").replace("(", "").split("|")[-1]

    response = requests.get(links[i], stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(f"{signer_name}{pla}{music_name}", "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print(f"{i+1} musics downloaded!")
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

print("""\n##########################
####Download Completed####
##########################""")
