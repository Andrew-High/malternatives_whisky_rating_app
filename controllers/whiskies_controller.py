from flask import Blueprint, Flask, redirect, render_template, request
from models.whisky import Whisky
import repositories.whisky_repository as whisky_repository
import repositories.distillery_repository as distillery_repository
import repositories.user_repository as user_repository

whiskies_blueprint = Blueprint("whisky", __name__)

# INDEX
@whiskies_blueprint.route("/whiskies")
def whiskies():
    whiskies = whisky_repository.select_all()
    dummy = 1
    user = user_repository.select(dummy)
    return render_template("whiskies/index.html", whiskies=whiskies, user = user)

# NEW
@whiskies_blueprint.route("/whiskies/new")
def new_whisky():
    distilleries = distillery_repository.select_all()
    return render_template("whiskies/new.html", distilleries = distilleries)

# CREATE
@whiskies_blueprint.route("/whiskies", methods=["POST"])
def create_whisky():
    name = request.form["name"]
    type = request.form["type"]
    flavour_profile = request.form["flavour_profile"]
    distillery_id = request.form["distillery_id"]
    distillery = distillery_repository.select(distillery_id)
    new_whisky = Whisky(name, type, flavour_profile, distillery)
    whisky_repository.save(new_whisky)
    return redirect("/whiskies")

# EDIT
@whiskies_blueprint.route("/whiskies/<id>/edit")
def edit_whisky(id):
    whisky = whisky_repository.select(id)
    return render_template("whiskies/edit.html", whisky = whisky)

# UPDATE
@whiskies_blueprint.route("/whiskies/<id>", methods = ["POST"])
def update_whisky(id):
    name = request.form["name"]
    type = request.form["type"]
    flavour_profile = request.form["flavour_profile"]
    distillery_id = request.form["distillery_id"]
    whisky = Whisky(name, type, flavour_profile, distillery_id, id)
    whisky_repository.update(whisky)

# DELETE
@whiskies_blueprint.route("/whiskies/<id>/delete", methods = ["POST"])
def delete_whisky(id):
    whisky_repository.delete(id)
    return redirect("/whiskies")