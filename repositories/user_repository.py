from db.run_sql import run_sql
from models.user import User

# CREATE
def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results
    user.id = id

# READ
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result["name"], result["reviews"], result["wishlist"], result["id"])
        users.append(user)
    return users

def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = User(result["name"], result["reviews"], result["wishlist"], result["id"])
    return user

# UPDATE
def update(user):
    sql = "UPDATE users SET (name, reviews, wishlist) VALUES (%s, %s, %s) WHERE id = %s"
    values = [user.name, user.reviews, user.wishlist, user.id]
    run_sql(sql, values)
    

# DELETE
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)
