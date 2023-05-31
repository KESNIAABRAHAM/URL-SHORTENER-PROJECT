from database import insert, get_url
import secrets
import string
import sqlite3

class Shortener:
    def __init__(self):
        pass

    def shorten(self, url):
        while True:
            short_url = self.generate_short_url()
            
            try:
                insert(url, short_url)
            except sqlite3.IntegrityError:
                continue
            
            break
        
        return short_url

    def generate_short_url(self):
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for i in range(7))

    def get_url(self, short_url):
        return get_url(short_url)

