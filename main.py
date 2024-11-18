import sqlalchemy as db
engine = db.create_engine('sqlite3:///books.db')
conn = engine.connect()
meta = db.MetaData()
books = db.Table('books', meta, autoload=True, autoload_with=engine)
print(db.select(books.c.author))

#SELECT books.author 
#FROM books
ordered = db.select(books.c.author).order_by(books.c.author)
authors = conn.execute(ordered)
authors.fetchall()