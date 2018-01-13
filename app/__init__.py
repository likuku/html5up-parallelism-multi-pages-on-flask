from flask import Flask
#from config import Config

app = Flask(__name__)
#app.config.from_object(__name__)
app.config.from_object('config')

from app import routes, models

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
