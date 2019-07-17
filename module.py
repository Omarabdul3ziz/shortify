import sqlite3, string
from random import choices

conn = sqlite3.connect('module.db', check_same_thread=False)
c = conn.cursor()

def shortify(long_url):
        characters = string.ascii_letters + string.digits
        short_url = 'tiny/' + ''.join(choices(characters, k=5))
        c.execute(f"""SELECT short_urls FROM urls WHERE short_urls = \'{short_url}\'""")
        result = c.fetchone()
        if result :
            shortify(long_url)

        else:
            c.execute(f"""INSERT INTO URLs(long_urls, short_urls) VALUES (\'{long_url}\', \'{short_url}\')""")
            conn.commit()
        return short_url


def longify(short_url):
    c.execute(f"""SELECT long_urls FROM urls WHERE short_urls = \'{short_url}\'""")
    result = c.fetchone()
    return result
