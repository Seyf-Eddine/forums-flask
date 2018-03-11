from flask import render_template, request, url_for, jsonify
from werkzeug.utils import redirect

from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods = ["POST"])
def topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["content"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__())

@app.route("/api/topic/delete/<int:id>")
def topic_remove(id):
    post = post_store.get_by_id(id)
    if post is not None:
        post_store.delete(id)
        return jsonify(post.__dict__())
    else:
        return "Error this topic does not exist"


@app.route("/api/topic/edit/<int:id>", methods = ["POST"])
def topic_modify(id):
    request_data = request.get_json()
    post = post_store.get_by_id(id)
    if post is not None:
        post.title = request_data["title"]
        post.content = request_data["content"]
        post_store.update(post)
        return jsonify(post.__dict__())
    else:
        return "This topic does not exist"


@app.route("/api/topic/show/<int:id>")
def topic_read(id):
    post = post_store.get_by_id(id)
    if post is not None:
        return jsonify(post.__dict__())
    else:
        return "This topic does not exist"
