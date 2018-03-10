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

@app.route("/api/topic/delete", methods = ["POST"])
def topic_remove():
    request_data = request.get_json()
    id = request_data["id"]
    if post_store.get_by_id(id) is not None:
        post_store.delete(id)
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/edit", methods = ["POST"])
def topic_modify():
    request_data = request.get_json()
    id = request_data["id"]
    post = post_store.get_by_id(id)
    if post is not None:
        post.title = request_data["title"]
        post.content = request_data["content"]
        post_store.update(post)
    return jsonify(post.__dict__())


@app.route("/api/topic/show", methods = ["POST"])
def topic_read():
    request_data = request.get_json()
    id = request_data["id"]
    post = post_store.get_by_id(id)
    if post is not None:
        return jsonify(post.__dict__())
    else:
        return "post doesn't exist"
