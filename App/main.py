import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta
from .forms import LoginForm
from .models.user import *

from App.database import init_db, get_migrate

from App.controllers import (
    setup_jwt
)

from App.views import (
    user_views,
    api_views
)

views = [
    user_views,
    api_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(days=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app, views)
    init_db(app)
    setup_jwt(app)
    app.app_context().push()
    return app
    
app = create_app()
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

migrate = get_migrate(app)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/login', methods=['POST'])
def loginAction():
    form = LoginForm()
    if form.validate_on_submit():
        data = request.form
        user = User.query.filter_by(username = data['username']).first()
        if user and user.check_password(data['password']):
            flash('Logged in successfully!')
            login_user(user)
            return redirect(url_for('admin'))
    flash('Invalid credentials!')
    return redirect(url_for('login'))

@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Logged out!')
    return redirect(url_for('.login'))

@app.route('/signup',methods=['POST'])
def signnup():
    userdata = request.get_json() # get userdata
    newuser = User(username=userdata['username'], email=userdata['email']) # create user object
    newuser.set_password(userdata['password']) # set password
    try:
        db.session.add(newuser)
        db.session.commit() # save user
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return 'username already exists' # error message
    return 'user created' # success

@app.route('/creatething<id>', methods=['POST'])
@jwt_required()
def create_todo(id):
    data = request.get_json()
    if id == 1:
      #create livestock
       newls = create_livestock(data['name'],data['quantity'],data['price'])
       db.session.add(newls)
       db.session.commit()
       return render_template('layout.html')
    if id == 2:
        #create crop
         crop = create_crop(data['name'],data['quantiity'],data['price'])
         db.session.add(crop)
         db.session.commit()
         return render_template('layout.html')
    if id == 3:
        #create chemicals
        new_chem = create_chemical(data['name'],data['quantiity'],data['npk1'],data['npk2'],data['npk3'])
        db.session.add(new_chem)
        db.session.commit()
        return render_template('layout.html')

    
#id in this case would be if the thing is a livestock, crop or chemcial 
@app.route('/allthings', methods=['GET'])
@jwt_required()
def get_task():
  tasks = User.query.filter_by(userid=current_identity.id).all()
  tasks = [User.toDict() for task in tasks]
  return json.dumps(tasks)


# rember to add update and delete for tasks or crops idk what to call it also we gotta have a distintion for plants and crops