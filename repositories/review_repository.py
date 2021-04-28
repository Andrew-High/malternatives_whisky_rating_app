from db.run_sql import run_sql
from models.review import Review
from models.whisky import Whisky
from models.distillery import Distillery
import repositories.whisky_repository as whisky_repository
import repositories.user_repository as user_repository
import pdb

# CREATE
def save(review):
    sql = "INSERT INTO reviews (rating, description, date, whisky_id, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [review.rating, review.description, review.date, review.whisky.id, review.user.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    review.id = id

# READ
def select_all():
    reviews = []
    sql = "SELECT * FROM reviews"
    results = run_sql(sql)
    for result in results:
        whisky_id = result["whisky_id"]
        whisky = whisky_repository.select(whisky_id)
        user_id = result["user_id"]
        user = user_repository.select(user_id)
        review = Review(whisky, user, result["rating"], result["date"], result["description"], result["id"])
        reviews.append(review)
    return reviews

def select(id):
    sql = "SELECT * FROM reviews WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    whisky = whisky_repository.select(result["whisky_id"])
    user = user_repository.select(result["user_id"])
    review = Review(whisky, user, result["rating"], result["date"], result["description"], result["id"])
    return review

# UPDATE
def update(review):
    sql = "UPDATE reviews SET (whisky_id, user_id, rating, date, description, id) VALUES (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [review.whisky.id, review.user.id, review.rating, review.date, review.id]
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
    sql = "SELECT * FROM reviews WHERE reviews.user_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for result in results:
        whisky = whisky_repository.select(result["whisky_id"])
        user = user_repository.select(result["user_id"])
        review = Review(whisky, user, result["rating"], result["date"], result["description"], result["id"])
        reviews.append(review)
    return reviews
