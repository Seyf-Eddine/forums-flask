from flask import Flask
from app.stores import MemberStore, PostStore
from app.dummy_data import seed_stores

member_store = MemberStore()
post_store = PostStore()

app = Flask(__name__)

from app.views import *
from app.api import *

seed_stores(member_store, post_store)
