from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Post, Character
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html", user = current_user)

@views.route("/new_post", methods=["GET", "POST"])
@login_required
def new_post():
    if request.method == "POST":
        post = request.form.get("post")
        if len(post) < 1:
            flash("Post is too short.", category = "error")
        else:
            new_post = Post(text = post, user_id = current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash("Post added", category = "success")

    return render_template("new_post.html", user = current_user)

@views.route("/new_character", methods=["GET", "POST"])
def new_character():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        character_img = request.form.get("character_img")
        import random
        chakra = random.randrange(25, 101)
        chakra_control = random.randrange(25, 101)
        strength = random.randrange(25, 101)
        speed = random.randrange(25, 101)
        if len(first_name) < 2:
            flash("Name is too short.", category = "error")
        elif character_img == "" or character_img == None:
            flash("Please put in a character image.", category = "error")
        else:
            if last_name:
                new_character = Character(first_name = first_name, last_name = last_name, chakra = chakra, chakra_control = chakra_control, speed = speed, strength = strength, character_img = character_img)
                db.session.add(new_character)
                db.session.commit()
    return render_template("new_character.html", user = current_user)


@views.route("/delete-post", methods=["POST"])
def delete_post():
    post = json.loads(request.data)
    post_id = post["postId"]
    post = Post.query.get(post_id)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()
    return jsonify({})