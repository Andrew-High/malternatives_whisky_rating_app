from db.run_sql import run_sql
from models.whisky import Whisky

# CREATE
def save(whisky):
    sql = "INSERT INTO whiskies (name, type, flavour_profile) VALUES (%s, %s) RETURNING id "
    values = [whisky.name, whisky,type, whisky.flavour_profile]
    results = run_sql(sql, values)
    id = results [0]["id"]
    whisky.id = id

# READ
def select_all():
    whiskies = []
    sql = "SELECT * FROM whiskies"
    results = run_sql(sql)
    for result in results:
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"])
        whiskies.append(whisky)
    return whiskies

def select(id):
    sql = "SELECT * FROM whiskies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    whisky = Whisky(result["name"], result["type"], result["flavour_profile"])
    return whisky

# UPDATE
def update(whisky):
    sql = "UPDATE whiskes SET (name, type, flavour_profile) = (%s, %s, %s) WHERE id = %s"
    values = [whisky.name, whisky.type, whisky.flavour_profile, whisky.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM whiskies"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM whiskies WHERE id = %s"
    values = [id]
    run_sql(sql, values)

