import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('urls.db')
        
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS urls (
                       short_url text PRIMARY KEY,
                       url text NOT NULL
                       );''')

def insert(url, short_url):
    sql = '''INSERT INTO urls (short_url, url)
             VALUES (?,?);'''
    db = Database()
    
    cur = db.conn.cursor()
    cur.execute(sql, (short_url, url))
    db.conn.commit()

    db.conn.close()

def get_url(short_url):
    sql = '''SELECT url FROM urls WHERE short_url = ?;'''
    db = Database()
    
    cur = db.conn.cursor()
    cur.execute(sql, (short_url,))
    
    row = cur.fetchone()
    db.conn.close()
    
    if row == None:
        return None
    else:
        return row[0]

