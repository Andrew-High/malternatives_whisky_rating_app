from db.run_sql import run_sql
from models.user import User
from models.whisky import Whisky
from models.distillery import Distillery
import repositories.whisky_repository as whisky_repository
import pdb

# CREATE
def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    user.id = id

# READ
def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result["name"], result["id"])
        users.append(user)
    return users

def select(id):
    pdb.set_trace
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = User(result["name"], result["id"])
    return user

# UPDATE
def update(user):
    sql = "UPDATE users SET (name, id) VALUES (%s, %s) WHERE id = %s"
    values = [user.name, user.id]
    run_sql(sql, values)
    
# DELETE
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# additional logic functions
def get_wishlist_of_user(id):
    whiskies = []
    sql = "SELECT whiskies.* FROM whiskies INNER JOIN wishlists ON wishlists.whisky_id = whiskies.id WHERE wishlists.user_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for result in results:
        distillery = whisky_repository.get_distillery(result["distillery_id"])
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"], distillery, result["id"])
        whiskies.append(whisky)
    return whiskies

def add_whisky_to_user_wishlist(user_id, whisky_id):
    sql = "INSERT INTO wishlists (user_id, whisky_id) VALUES (%s, %s) RETURNING id"
    values = [user_id, whisky_id]
    results = run_sql(sql, values)
    wishlist_id = id
    return wishlist_id
