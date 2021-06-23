from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class FlaskApp():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://tmvudmtuvscrrg:cacd0b0c622ef4befe71490e09f48c7b9ea3db67868476a39d071708faf27cf9@ec2-35-169-92-231.compute-1.amazonaws.com:5432/d9oga7lftk34ur"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)

flaskApp = FlaskApp()
