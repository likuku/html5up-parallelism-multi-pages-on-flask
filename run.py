# from http://flask.pocoo.org/ tutorial
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    #return "Hello World!"
    return render_template('index.html',
                           logo = 'likuku',
                           img='https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg',
                           loop=[{'w':'200','simg':'images/thumbs/01.jpg'},
                                 {'w':'150','simg':'images/thumbs/02.jpg'},
                                 {'w':'230','simg':'images/thumbs/03.jpg'},
                                 {'w':'170','simg':'images/thumbs/04.jpg'},
                                 {'w':'260','simg':'images/thumbs/05.jpg'}])

@app.route("/project1") # take note of this decorator syntax, it's a common pattern
def project():
    #return "Hello World!"
    return render_template('project.html',
                           logo = 'likuku',
                           loop=[{'w':'200','simg':'images/thumbs/01.jpg'},
                                 {'w':'150','simg':'images/thumbs/02.jpg'},
                                 {'w':'230','simg':'images/thumbs/03.jpg'},
                                 {'w':'170','simg':'images/thumbs/04.jpg'},
                                 {'w':'260','simg':'images/thumbs/05.jpg'}])

if __name__ == "__main__":
    app.run()
