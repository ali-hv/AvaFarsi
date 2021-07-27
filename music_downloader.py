from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib
import regex
import os
import pyfiglet
from random import randint
from time import sleep
import platform 



plt = platform.system()

if plt == "Windows":
    pla = '\\'
elif plt == "Linux":
    pla = '/'

d = 1

print('#'*60)
print(pyfiglet.figlet_format('Music Downloader', font='slant'))
print('Made by Ali Hosseinverdi')
print('#'*60)


def md():
    a = 1
    c = 1
    
    fname = input('\nFirst Name : ')
    lname = input('Last Name : ')
    fname = fname.replace('ي', 'ی')
    lname = lname.replace('ي', 'ی')
    lname2 = lname
    fname = fname.replace(' ', '-')
    lname = lname.replace(' ', '-')

    name = fname+' '+lname2

    where = input('\nFrom which site ?(1 for upmusics.com, 2 for music-fa.com, 3 for jenabmusic.com) : ')
    if where == '1':
        url = "https://upmusics.com/tag/%s-%s/" %(fname,lname)
    elif where == '2':
        url = "https://music-fa.com/artist/%s-%s/" %(fname,lname)
    else:
        url = "https://www.jenabmusic.com/category/music-artist/%s-%s/" %(fname,lname)
        c = 0
        
    print('\nSearching...')

    site = requests.get(url)
    status = site.status_code
    if status == 404:
        br()
    else:
        pass
    site = site.text

    bs = BeautifulSoup(site, 'html.parser')

    pages = bs.find_all('a', {'class' : 'last'})
    if pages == []:
        try:
            if c == 0:
                pages = bs.find_all('a', {'class' : 'page-numbers'})
                pages = regex.sub('.*\/(\d+).*', '\g<1>', str(pages[1]))
                if int(pages) > 100:
                    br()
            else:
                pages = bs.find_all('a', {'class' : 'page'})
                pages = regex.sub('.*"(.)".*', '\g<1>', str(pages[-1]))
        except IndexError:
            musics = bs.find_all('audio')
            musics = str(musics)

            bs = BeautifulSoup(musics, 'html.parser')

            links = []

            for i in range (10):
                try:
                    if c == 0:
                        link = bs.findAll('source')[i]
                        links.append(link.get("src"))
                    else:
                        link = bs.findAll('audio')[i]
                        links.append(link.get("src")) 
                except IndexError:
                    break
            
            music = len(links)

            sizes = []

            for i in range(music):
                try:
                    url = links[i]
                except IndexError:
                    break
                except UnicodeEncodeError:
                    break
                size = urllib.request.urlopen(url)
                length = size.length
                sizes.append(length)
                num = sizes.count(length)
                if num == 2:
                    b = links[i]
                    links.remove(b)
                else:
                    continue

            music = len(links)

            number = int(input('\nThere are %i songs by this singer . How many do you want to download ? : ' %(music)))

            

            if number > 0:
                try:
                    path = os.getcwd() + pla + name
                    files = os.mkdir(path)
                except FileExistsError:
                    rand = str(randint(1,50))
                    path = os.getcwd() + pla + name + rand
                    files = os.mkdir(path)

                print('\nDownloading...\n')

            for i in range(number):
                url = links[i]
                print('-'*30)
                r = requests.get(url, allow_redirects=True)
                open(f'%s{pla}%s%i.mp3' %(path, name, i+1), 'wb').write(r.content)

                print('%i music was downloaded' %(i+1))

            print('-'*30)
            print('''\n########################
###Download completed###
########################''')
            quit(input('\nPress Enter to exit ...'))

    else:
        pages = regex.sub('.*\/(\d+)\/.*', '\g<1>', str(pages))

    if a == 0:
        pass
    else:
        pages = int(pages)
        musics = bs.find_all('audio')
        musics = str(musics)
        bs = BeautifulSoup(musics, 'html.parser')

        links = []

        for i in range (10):
            try:
                if c == 0:
                    link = bs.findAll('source')[i]
                    links.append(link.get("src"))
                else:
                    link = bs.findAll('audio')[i]
                    links.append(link.get("src")) 
            except IndexError:
                break
        if pages >= 2:
            for i in range (2,pages+1):
                if where == '1':
                    url = "https://upmusics.com/tag/%s-%s/page/%i" %(fname,lname,i)
                elif where == '2':
                    url = "https://music-fa.com/artist/%s-%s/page/%i" %(fname,lname,i)
                else:
                    url = "https://www.jenabmusic.com/category/music-artist/%s-%s/page/%i" %(fname,lname,i)
                site = requests.get(url)
                site = site.text

                bs = BeautifulSoup(site, 'html.parser')
                musics = bs.find_all('audio')
                musics = str(musics)

                bs = BeautifulSoup(musics, 'html.parser')

                for i in range (10):
                    try:
                        if c == 0:
                            link = bs.findAll('source')[i]
                            links.append(link.get("src"))
                        else:
                            link = bs.findAll('audio')[i]
                            links.append(link.get("src")) 
                    except IndexError:
                        break

        music = len(links)
        sizes = []
        
        for i in range(music):
            try:
                url = links[i]
            except IndexError:
                break
            try:
                size = urllib.request.urlopen(url)
            except urllib.error.HTTPError:
                break
            except UnicodeEncodeError:
                break
            length = size.length
            sizes.append(length)
            num = sizes.count(length)
            if num == 2:
                b = links[i]
                links.remove(b)
            else:
                pass

        music = len(links)
        number = int(input('\nThere are %i songs by this singer . How many do you want to download ? : ' %(music)))

        if number > 0:
            try:
                path = os.getcwd() + pla + name
                files = os.mkdir(path)
            except FileExistsError:
                rand = str(randint(1,50))
                path = os.getcwd() + pla + name + rand
                files = os.mkdir(path)

            print('\nDownloading...\n')

        for i in range(number):
            url = links[i]
            print('-'*30)
            r = requests.get(url, allow_redirects=True)
            open(f'%s{pla}%s%i.mp3' %(path, name, i+1), 'wb').write(r.content)

            print('%i music was downloaded' %(i+1))

        print('-'*30)
        print('''\n########################
###Download completed###
########################''')
        quit(input('\nPress Enter to exit ...'))

def br():
    print('\nNo song found!!!')
    print('\nTry with give url manual(line29) or try with another site')
    again = input('\nDo you want to use again ?(y/n): ')
    if again == 'y':
        md()
    else:
        print('\ngood by (:')
        d = 0
        quit()
if d == 1:
    md()
