import string
import sqlite3
from random import choices

conn = sqlite3.connect('module.db')
c = conn.cursor()

def shrink(long_url):
        characters = string.ascii_letters + string.digits
        short_url = 'tiny/' + ''.join(choices(characters, k=5))
        c.execute(f'SELECT short_urls FROM urls WHERE short_urls = "{short_url}"')
        result = c.fetchone()
        if result :
            shrink(long_url)

        else:
            c.execute(f'INSERT INTO URLs(long_urls, short_urls) VALUES ("{long_url}","{short_url}")')
            conn.commit()

shrink('www.google.com')