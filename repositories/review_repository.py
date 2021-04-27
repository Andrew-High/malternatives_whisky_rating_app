from db.run_sql import run_sql
from models.review import Review
from models.whisky import Whisky
from models.distillery import Distillery
import repositories.whisky_repository as whisky_repository
import pdb

# CREATE
def save(review):
    sql = "INSERT INTO reviews (whisky_id, user_id, rating, date, description) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [review.whisky_id, review.user_id, review.rating, review.date, review.description]
    results = run_sql(sql, values)
    id = results[0]["id"]
    review.id = id

# READ
def select_all():
    reviews = []
    sql = "SELECT * FROM reviews"
    results = run_sql(sql)
    for result in results:
        review = Review(result["whisky_id"], result["user_id"], result["rating"], result["date"], result["description"], result["id"])
        reviews.append(review)
    return reviews

def select(id):
    sql = "SELECT * FROM reviews WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    review = Review(result["whisky_id"], result["user_id"], result["rating"], result["date"], result["description"], result["id"])
    return review

# UPDATE
def update(review):
    sql = "UPDATE reviews SET (whisky_id, user_id, rating, date, description, id) VALUES (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [review.whisky_id, review.user_id, review.rating, review.date, review.id]
    run_sql(sql, values)
    
# DELETE
def delete_all():
    sql = "DELETE FROM reviews"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM reviews WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# additional logic functions
def get_reviews_of_user(id):
    reviews = []
    sql = "SELECT reviews.* WHERE reviews.user_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for result in results:
        review = Review(result["whisky_id"], result["user_id"], result["rating"], result["date"], result["description"], result["id"])
        reviews.append(review)
    return reviews
