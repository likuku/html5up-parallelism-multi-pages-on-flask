from app import app
from sqlalchemy import Column, Integer, String
from app.database import Base
import sqlite3

class Setting(Base):
    __tablename__ = 'setting'
    id = Column(Integer, primary_key=True)
    key = Column(String(50))
    value = Column(String(255))

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<Setting (key="%s", value="%s")>' % (self.key, self.value)

#####
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

from contextlib import closing
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode())
        db.commit()

from flask import g
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

def get_settings():
    #_cur = g.db.execute('SELECT value FROM setting WHERE key = "logo"')
    #_logo = [row[0] for row in _cur.fetchall()][0]
    #_cur = g.db.execute('SELECT value FROM setting WHERE key = "bg_img"')
    #_bg_img = [row[0] for row in _cur.fetchall()][0]
    _logo = (Setting.query.filter(Setting.key == 'logo').first()).value
    _bg_img = (Setting.query.filter(Setting.key == 'bg_img').first()).value
    _settings = {'logo':_logo, 'bg_img':_bg_img}
    return(_settings)

def get_projects():
    _cur = g.db.execute('SELECT id,name FROM project ORDER BY id ASC')
    return([dict(href='/project/id/' + str(row[0]),project_name=row[1]) for row in _cur.fetchall()])

def get_contacts():
    _cur = g.db.execute('SELECT href,class,label FROM contact ORDER BY id ASC')
    _contacts = []
    for row in _cur.fetchall():
        _contacts.append({'href':row[0],'class':row[1],'label':row[2]})
    return(_contacts)

def get_photos_index():
    _cur = g.db.execute('SELECT href,width,src FROM photo ORDER BY id ASC')
    return([dict(href=row[0],width=row[1],simg=row[2]) for row in _cur.fetchall()])

def get_photos_project(_project_id):
    _sql = 'SELECT photo.href,photo.width,photo.src FROM photo WHERE \
        photo.id IN (select projects_photos.photo_id from projects_photos WHERE \
        projects_photos.project_id = %d) ORDER BY photo.id ASC' % _project_id
    _cur = g.db.execute(_sql)
    return([dict(href=row[0],width=row[1],simg=row[2]) for row in _cur.fetchall()])
