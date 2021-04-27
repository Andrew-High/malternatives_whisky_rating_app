import pdb
from flask import Blueprint, Flask, redirect, render_template, request
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("user", __name__)

# INDEX
@users_blueprint.route("/users", methods = ["GET"])
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

# NEW
@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html")

# CREATE
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form["name"]
    new_user = User(name)
    user_repository.save(new_user)
    return redirect("/users")

# EDIT
@users_blueprint.route("/users/<id>/edit")
def edit_users(id):
    user = user_repository.select(id)
    return render_template("users/edit.html", user = user)

# UPDATE
@users_blueprint.route("/users/<id>", methods = ["POST"])
def update_distillery(id):
    name = request.form["name"]
    user = Users(name, id)
    user_repository.update(user)

# DELETE
@users_blueprint.route("/users/<id>/delete", methods = ["POST"])
def delete_user(id):
    user_repository.delete(id)
    return redirect("/users")

# additional logic functions
# individual user
@users_blueprint.route("/users/<id>")
def user(id):
    user = user_repository.select(id)
    return render_template("users/individual.html", user = user)

# recall individual user's wishlist
@users_blueprint.route("/users/<id>/wishlist")
def user_wishlist(id):
    pdb.set_trace
    user = user_repository.select(id)
    user_wishlist = user_repository.get_wishlist_of_user(id)
    return render_template("users/wishlist.html", user = user, user_wishlist = user_wishlist)