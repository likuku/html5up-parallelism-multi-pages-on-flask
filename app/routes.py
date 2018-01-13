from flask import render_template
from app import app
from app.models import *

#init_db()

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
