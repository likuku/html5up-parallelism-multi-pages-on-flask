from app import app
from app.models import *
from flask import Flask
from flask_admin import Admin
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='Admin', template_mode='bootstrap3')
# Add administrative views here

#class CustomModelView(ModelView):
#    """View function of Flask-Admin for Models page."""
#    pass
class ModeViewWithDisplay(ModelView):
    form_choices = {
    'display': [
        ('Yes', 'Yes'),
        ('No', 'No')
        ]
    }

class ModelViewOnlyEdit(ModeViewWithDisplay):
    can_delete = False  # disable model deletion
    can_create = False # disable model create
    can_edit = False
    page_size = 50  # the number of entries to display on the list view
    #can_view_details = True

class ModelViewSetting(ModelViewOnlyEdit):
    column_editable_list = ['value']

class ModelViewContact(ModelViewOnlyEdit):
    column_exclude_list = ['class_name' ]
    column_editable_list = ['href','display']
    column_labels = dict(href='Link')

class ModelViewProject(ModeViewWithDisplay):
    can_edit = False
    column_editable_list = ['name','display']
    #can_view_details = True

class ModelViewProjectsPhotos(ModeViewWithDisplay):
    column_display_pk = True # optional, but I like to see the IDs in the list
    #column_display_all_relations = True
    #column_editable_list = ['name','display']
    #column_formatters = dict(mps=lambda v, c, m, p: (m.project_photo_name_str))

class ModelViewPhoto(ModeViewWithDisplay):
    can_edit = True
    column_list = ('display',
                   'show_on_homepage',
                   'project_id',
                   'description',
                   'href',
                   'src',
                   'width')
    column_editable_list = ['width',
                            'description',
                            'project_id',
                            'show_on_homepage',
                            'display']
    column_labels = dict(href='BigImage',
                         src='Icon',
                         width='IconWidth',
                         description='Title',
                         project_id='Project',
                         show_on_homepage='HomePage')
    #can_view_details = True
    # better choices for project_id:
    project_id_list_raw = Project.query.all()
    if project_id_list_raw is not None:
        _list = []
        for _project in project_id_list_raw:
            _list.append((str(_project.id),_project.name))
        form_choices = {
        'project_id': _list
        }
    else:
        pass

from app.database import db_session
admin.add_view(ModelViewSetting(Setting, db_session))
admin.add_view(ModelViewContact(Contact, db_session))
admin.add_view(ModelViewProject(Project, db_session))
admin.add_view(ModelViewPhoto(Photo, db_session))
#admin.add_view(ModelViewProjectsPhotos(Projects_Photos, db_session))
