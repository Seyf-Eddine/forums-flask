from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
#app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "my_database.db")}"""
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://ygyockkrbjjfee:2f4bf298746cf7eb11e07c2d0e55c48265f867fb5c4f535c0db21dd58fe90f6d@ec2-174-129-28-38.compute-1.amazonaws.com:5432/d3kb397gms4402'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import stores, dummy_data

member_store = stores.MemberStore()
post_store = stores.PostStore()
dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api
