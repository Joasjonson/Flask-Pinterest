from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("db_url")
# app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://@DESKTOP-DU0URSN/TESTE?driver=ODBC+Driver+17+for+SQL+Server"
app.config["SECRET_KEY"] = "43a20b740bed232291d874980fe79f"
app.config["UPLOAD_FOLDER"] = "static/picture_posts"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "index"

from mypinterest import routes
