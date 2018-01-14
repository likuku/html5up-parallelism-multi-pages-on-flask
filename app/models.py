from app import app
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Setting(Base):
    __tablename__ = 'setting'
    id = Column(Integer, primary_key=True)
    key = Column(String(50), nullable=False, unique=True)
    value = Column(String)

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<Setting (key="%r", value="%r")>' % (self.key, self.value)

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Project (name="%r")>' % (self.name)

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    href = Column(String ,nullable=False)
    class_name = Column(String(50) ,nullable=False)
    label = Column(String(50) ,nullable=False)

    def __init__(self, href=None, class_name=None, label=None):
        self.href = href
        self.class_name = value
        self.label = label

    def __repr__(self):
        return '<Contact (href="%r", class_name="%r", label="%r")>' % (
            self.href,self.class_name,self.label)

class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    href = Column(String, nullable=False, unique=True)
    width = Column(Integer, nullable=False)
    src = Column(String, nullable=False, unique=True)

    def __init__(self, href=None, width=None, src=None):
        self.href = href
        self.width = value
        self.src = src

    def __repr__(self):
        return '<Photo (href="%r", width="%r", src="%r")>' % (
            self.href,self.width,self.src)


class Projects_Photos(Base):
    __tablename__ = 'projects_photos'
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)
    photo_id = Column(Integer, ForeignKey('photo.id'), primary_key=True)

    def __init__(self, project_id=None, photo_id=None):
        self.project_id = project_id
        self.photo_id = photo_id

    def __repr__(self):
        return '<Projects_Photos (project_id="%r", photo_id="%r")>' % (
            self.project_id,self.photo_id)

#####
import sqlite3
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
    _cur = g.db.execute('SELECT href,class_name,label FROM contact ORDER BY id ASC')
    return([dict(href=row[0],class_name=row[1],label=row[2]) for row in _cur.fetchall()])

def get_photos_index():
    _cur = g.db.execute('SELECT href,width,src FROM photo ORDER BY id ASC')
    return([dict(href=row[0],width=row[1],simg=row[2]) for row in _cur.fetchall()])

def get_photos_project(_project_id):
    _sql = 'SELECT photo.href,photo.width,photo.src FROM photo WHERE \
        photo.id IN (select projects_photos.photo_id from projects_photos WHERE \
        projects_photos.project_id = %d) ORDER BY photo.id ASC' % _project_id
    _cur = g.db.execute(_sql)
    return([dict(href=row[0],width=row[1],simg=row[2]) for row in _cur.fetchall()])
