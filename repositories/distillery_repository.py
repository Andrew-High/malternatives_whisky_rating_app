from db.run_sql import run_sql
from models.distillery import Distillery
from models.whisky import Whisky
import repositories.whisky_repository as whisky_repository

# CREATE
def save (distillery):
    sql = "INSERT INTO distilleries (name, region, founded) VALUES (%s, %s, %s) RETURNING *"
    values = [distillery.name, distillery.region, distillery.founded]
    results = run_sql(sql, values)
    id = results[0]["id"]
    distillery.id = id

# READ
def select_all():
    distilleries = []
    sql = "SELECT * FROM distilleries"
    results = run_sql(sql)
    for result in results:
        distillery = Distillery(result["name"], result["region"], result["founded"])
        distilleries.append(distillery)
    return distilleries

def select(id):
    sql = "SELECT * FROM distilleries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    distillery = Distillery(result["name"], result["region"], result["founded"])
    return distillery

# UPDATE
def update(distillery):
    sql = "UPDATE distilleries SET (name, region, founded, whiskies) = (%s, %s, %s, %s) WHERE id = %s"
    values = [distillery.name, distillery.region, distillery.founded]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM distilleries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM distilleries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# additional logic functions
def select_whiskies_of_distillery(id):
    whiskies = []
    sql = "SELECT * FROM whiskies WHERE distillery_id = %s"
    values = [id]
    results = run_sql(sql,values)
    for result in results:
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"], result["id"], result["distillery_id"])
        whiskies.append(whisky)
    return whiskies
