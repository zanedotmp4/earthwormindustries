import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta
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

# Routes start here

# Main Page. Login

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        user = User.query.filter_by(username = request("username")).first()
        if user and user.check_password(request("password")):
            flash('Logged in successfully!')
            login_user(user)
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials!')
            return render_template('index.html')

# Backend Routes

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Logged out!')
    return redirect(url_for('home'))
