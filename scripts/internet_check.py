import urllib

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