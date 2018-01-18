from app import app
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from app.database import Base
from sqlalchemy.orm import relationship, backref

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

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    class_name = Column(String(50), nullable=False)
    label = Column(String(50), nullable=False)
    href = Column(String, nullable=False)
    example = Column(String, nullable=True)
    display = Column(String, nullable=False, default='Yes')

    def __init__(self, href=None, class_name=None, label=None):
        self.href = href
        self.class_name = class_name
        self.label = label

    def __repr__(self):
        return '<Contact (href="%r", class_name="%r", label="%r", display="%r")>' % (
            self.href,self.class_name,self.label,self.display)
'''
projects_photos = Table('project_photos', Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('photo_id',Integer, ForeignKey('photo.id'))
)
'''
class Projects_Photos(Base):
    __tablename__ = 'projects_photos'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    photo_id = Column(Integer, ForeignKey('photo.id'))
    #project_id = Column(Integer, nullable=False)
    #photo_id = Column(Integer, nullable=False)
    #project = relationship('Project', back_populates='photos')
    #photo = relationship('Photo', back_populates='projects')
    #project = relationship('Project',cascade_backrefs=True)
    #photo = relationship('Photo',cascade_backrefs=True)

    #def __init__(self, project_id=None, photo_id=None):
    #    self.project_id = project_id
    #    self.photo_id = photo_id

    def __repr__(self):
        return '<Projects_Photos (project_id="%r", photo="%r")>' % (self.project_id,self.photo)


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    display = Column(Integer, nullable=False, default=1)
    #photos = relationship('Projects_Photos', back_populates='project')
    #photos = relationship('Projects_Photos',uselist=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Project (id="%d", name="%r", display="%r")>' % (
            self.id,self.name,self.display)

class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    href = Column(String, nullable=False, unique=True)
    width = Column(Integer, nullable=False)
    src = Column(String, nullable=False, unique=True)
    project_id = Column(Integer)
    show_on_homepage = Column(String, nullable=False, default='Yes')
    display = Column(String, nullable=False, default='Yes')
    #projects = relationship('Projects_Photos', back_populates='photo')

    def __init__(self, href=None, width=None, src=None, project_id=None):
        self.href = href
        self.width = width
        self.src = src
        self.project_id = project_id

    def __repr__(self):
        return '<Photo (id="%d", href="%r", width="%r", src="%r", display="%r")>' % (
            self.id,self.href,self.width,self.src,self.display)



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
    _cur = g.db.execute('SELECT href,class_name,label FROM contact WHERE display = "Yes" ORDER BY id ASC')
    return([dict(href=row[0],class_name=row[1],label=row[2]) for row in _cur.fetchall()])

def get_photos_index():
    _cur = g.db.execute('SELECT href,width,src FROM photo ORDER BY id ASC')
    return([dict(href=row[0],width=row[1],simg=row[2]) for row in _cur.fetchall()])

def get_photos_project(_project_id):
    #_sql = 'SELECT photo.href,photo.width,photo.src FROM photo WHERE \
    #    photo.id IN (select projects_photos.photo_id from projects_photos WHERE \
    #    projects_photos.project_id = %d) ORDER BY photo.id ASC' % _project_id
    _sql = 'SELECT photo.href,photo.width,photo.src FROM photo WHERE \
        project_id = %d ORDER BY photo.id ASC' % _project_id
    _cur = g.db.execute(_sql)
    return([dict(href=row[0],width=row[1],simg=row[2]) for row in _cur.fetchall()])
