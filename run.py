# from http://flask.pocoo.org/ tutorial
from flask import Flask
from flask import render_template
app = Flask(__name__)

logo = 'likuku'
bg_img = 'https://wx4.sinaimg.cn/large/4d48a5a9gy1fn2e6ivc6oj21kw1fk1kx.jpg'
img ='https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg'

projects = [{'href':'project1','project_name':'project1'},
            {'href':'#','project_name':'project2'},
            {'href':'#','project_name':'project3'},
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
                {'width':'230','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/03.jpg'},
                {'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/04.jpg'},
                {'width':'260','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/05.jpg'},
                {'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/06.jpg'},
                {'width':'260','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/07.jpg'},
                {'width':'230','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/08.jpg'}]

photos_project1 = [{'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/01.jpg'},
                {'width':'150','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/02.jpg'},
                {'width':'230','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/03.jpg'},
                {'width':'200','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/04.jpg'},
                {'width':'260','href':'https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','simg':'images/thumbs/05.jpg'}]

@app.route("/") # take note of this decorator syntax, it's a common pattern
def index():
    return render_template('index.html',
                           logo = logo,
                           bg_img = bg_img,
                           photos = photos_index,
                           contacts = contacts,
                           projects = projects
                           )

@app.route("/project1") # take note of this decorator syntax, it's a common pattern
def project():
    return render_template('project.html',
                           logo = logo,
                           bg_img = bg_img,
                           photos = photos_project1,
                           contacts = contacts,
                           projects = projects
                           )

if __name__ == "__main__":
    app.run()
