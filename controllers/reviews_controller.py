import pdb
from flask import Blueprint, Flask, redirect, render_template, request
from models.user import User
import repositories.review_repository as review_repository
import repositories.whisky_repository as whisky_repository
import repositories.user_repository as user_repository

users_blueprint = Blueprint("review", __name__)

# INDEX
@reviews_blueprint.route("/reviews", methods = ["GET"])
def reviews():
    reviews = review_repository.select_all()
    return render_template("reviews/index.html", reviews = reviews)

# NEW
@reviews_blueprint.route("/reviews/new")
def new_review():
    return render_template("reviews/new.html")

# CREATE
@reviews_blueprint.route("/reviews", methods=["POST"])
def create_review():
    whisky_id = request.form["whisky_id"]
    user_id = request.form["user_id"]
    rating = request.form["rating"]
    date = request.form["date"]
    description = request.form["description"]
    new_review = Review(whisky_id, user_id, rating, date, description)
    review_repository.save(new_review)
    return redirect("/reviews")

# EDIT
@reviews_blueprint.route("/reviews/<id>/edit")
def edit_reviews(id):
    review = review_repository.select(id)
    return render_template("reviews/edit.html", review = review)

# UPDATE
@reviews_blueprint.route("/reviews/<id>", methods = ["POST"])
def update_review(id):
    whisky_id = request.form["whisky_id"]
    user_id = request.form["user_id"]
    rating = request.form["rating"]
    date = request.form["date"]
    description = request.form["description"]
    id = request.form["id"]
    review = Review(whisky_id, user_id, rating, date, description, id)
    review_repository.update(review)

# DELETE
@reviews_blueprint.route("/reviews/<id>/delete", methods = ["POST"])
def delete_review(id):
    review_repository.delete(id)
    return redirect("/reviews")

# additional logic functions
# individual review
@reviews_blueprint.route("/reviews/<id>")
def review(id):
    review = review_repository.select(id)
    return render_template("reviews/individual.html", review = review)