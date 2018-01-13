# from http://flask.pocoo.org/ tutorial
from flask import Flask
from flask import render_template

import os
import sqlite3

# configuration
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'instance', 'data.db')
DEBUG = True
SECRET_KEY = 'DEV SECRET_KEY'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

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
'''
logo = 'likuku'
bg_img = 'https://wx4.sinaimg.cn/large/4d48a5a9gy1fn2e6ivc6oj21kw1fk1kx.jpg'
'''

def get_settings():
    _cur = g.db.execute('SELECT value FROM setting WHERE key = "logo"')
    _logo = [row[0] for row in _cur.fetchall()][0]
    _cur = g.db.execute('SELECT value FROM setting WHERE key = "bg_img"')
    _bg_img = [row[0] for row in _cur.fetchall()][0]
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
'''
projects = [{'href':'/project/id/1','project_name':'project1'},
            {'href':'/project/id/2','project_name':'project2'},
            {'href':'/project/id/3','project_name':'project3'},
            {'href':'#','project_name':'project4'}]

contacts = [{'href':'#','class':'icon fa-twitter','label':'Twitter'},
            {'href':'#','class':'icon fa-instagram','label':'Instagram'},
            {'href':'#','class':'icon fa-facebook','label':'Facebook'},
            {'href':'#','class':'icon fa-dribbble','label':'Dribbble'},
            {'href':'#','class':'icon fa-pinterest','label':'Pinterest'},
            {'href':'#','class':'icon fa-weixin','label':'Wechat'},
            {'href':'#','class':'icon fa-envelope','label':'Email'}]

photos_index = [{'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/01.jpg'},
                {'width':'150','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/02.jpg'},
                {'width':'230','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/08.jpg'}]

photos_project1 = [{'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/01.jpg'},
                   {'width':'150','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/02.jpg'},
                   {'width':'150','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/03.jpg'}]

photos_project2 = [{'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/02.jpg'},
                   {'width':'150','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/03.jpg'},
                   {'width':'260','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/04.jpg'}]

projects_photos = {1:photos_project1,2:photos_project2}
'''

@app.route("/") # take note of this decorator syntax, it's a common pattern
@app.route('/index')
def index():
    _projects = get_projects()
    _settings = get_settings()
    _contacts = get_contacts()
    _photos = get_photos_index()
    return render_template('index.html',
                           logo = _settings['logo'],
                           bg_img = _settings['bg_img'],
                           photos = _photos,
                           contacts = _contacts,
                           projects = _projects
                           )

@app.route("/project/id/<int:project_id>") # take note of this decorator syntax, it's a common pattern
def project(project_id):
    _projects = get_projects()
    _settings = get_settings()
    _contacts = get_contacts()
    _projects_photos = get_photos_project(project_id)
    return render_template('project.html',
                           logo = _settings['logo'],
                           bg_img = _settings['bg_img'],
                           photos = _projects_photos,
                           contacts = _contacts,
                           projects = _projects
                           )


if __name__ == "__main__":
    init_db()
    app.run()
