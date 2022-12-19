import urllib
import socket

def check(self):
    try:
        urllib.request.urlopen('https://music-fa.com', timeout=10)
        return True
    except urllib.error.URLError: 
        return False
    except TimeoutError:
        try:
            urllib.request.urlopen('https://music-fa.com', timeout=10)
        except urllib.error.URLError: 
            return False
        except TimeoutError:
            return False
    except socket.timeout:
        try:
            urllib.request.urlopen('https://music-fa.com', timeout=20)
        except:
            return False
    except:
        return False