import pdb
from flask import Blueprint, Flask, redirect, render_template, request
from models.distillery import Distillery
import repositories.distillery_repository as distillery_repository
import repositories.whisky_repository as whisky_repository

distilleries_blueprint = Blueprint("distillery", __name__)

# INDEX
@distilleries_blueprint.route("/distilleries", methods = ["GET"])
def distilleries():
    distilleries = distillery_repository.select_all()
    for distillery in distilleries:
        whiskies = whisky_repository.select_by_distillery(distillery.id)
        if whiskies == None:
            whiskies = []
    return render_template("distilleries/index.html", distilleries=distilleries)

# NEW
@distilleries_blueprint.route("/distilleries/new")
def new_distillery():
    return render_template("distilleries/new.html")

# CREATE
@distilleries_blueprint.route("/distilleries", methods=["POST"])
def create_distillery():
    # pdb.set_trace()
    name = request.form["name"]
    region = request.form["region"]
    founded = request.form["founded"]
    new_distillery = Distillery(name, region, founded)
    distillery_repository.save(new_distillery)
    return redirect("/distilleries")

# EDIT
@distilleries_blueprint.route("/distilleries/<id>/edit")
def edit_distilleries(id):
    distillery = distillery_repository.select(id)
    return render_template("distilleries/edit.html", distillery = distillery)

# UPDATE
@distilleries_blueprint.route("/distilleries/<id>", methods = ["POST"])
def update_distillery(id):
    name = request.form["name"]
    region = request.form["region"]
    founded = request.form["founded"]
    distillery = Distillery(name, region, founded, id)
    distillery_repository.update(distillery)

# DELETE
@distilleries_blueprint.route("/distilleries/<id>/delete", methods = ["POST"])
def delete_distillery(id):
    distillery_repository.delete(id)
    return redirect("/distilleries")