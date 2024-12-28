from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename #To upload the image and handling the file
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # to connect to database file name blog.db
db = SQLAlchemy(app) # created db object to interact with database
class Post(db.Model): #defined  a model about post for database 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<Post {self.title}>'

with app.app_context(): #within the flask app context to interact with database
        db.create_all() #to create Post table based on the Post class

#login
app.secret_key = 'google.com/u/1/app/0933317a82dc8150?hl=en-IN'

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect('/')
        else:
            return 'Invalid credetials, pleasy try again.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@app.route('/')
def home():
    posts = Post.query.all() #fetch all the query from the database from the Post table and return it as list of Post objects
    return render_template('index.html',posts=posts) #render index.html and pass the posts to it

#For uploading the images
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.split('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add',methods=['POST','GET'])
def add_post():
    if 'logged_in' not in session:
        return redirect('/login')
    title = request.form['title']
    content = request.form['content']

    if 'image' not in request.files:
        return 'No image uploaded',400

    image = request.files['image']

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    else:
        filename = None

    new_post = Post(title=title, content=content, image=filename)
    db.session.add(new_post)
    db.session.commit()
    return redirect('/')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)

    return render_template('post.html',post=post)

@app.route('/post/delete/<int:post_id>',methods=['POST'])
def delete_post(post_id):
    if 'logged_in' not in session:
        return redirect('/login')
    post = Post.query.get_or_404(post_id)
    
    if post.image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], post.image)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
