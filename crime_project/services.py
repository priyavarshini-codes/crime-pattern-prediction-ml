import database as db

def add_crime(date,ctype,lat,lon,loc):
    db.insert((date,ctype,lat,lon,loc))

def get_data():
    return db.fetch_df()

def remove(id):
    db.delete(id)
