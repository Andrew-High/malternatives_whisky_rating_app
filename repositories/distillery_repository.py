from db.run_sql import run_sql
from models.distillery import Distillery
from models.whisky import Whisky
import repositories.whisky_repository as whisky_repository

# CREATE
def save (distillery):
    sql = "INSERT INTO distilleries (name, region, founded, whiskies) VALUES (%s. %s, %s, %s) RETURNING id"
    values = [distillery.name, distillery.region, distillery.founded, distillery.whiskies]
    results = run_sql(sql, values)
    id = results[0]["id"]
    distillery.id = id

# READ
def select_all():
    distilleries = []
    sql = "SELECT * FROM distilleries"
    results = run_sql(sql)
    for result in results:
        whiskies = []
        for whisky in result.whiskies:
            whiskies.append(whisky_repository.select(result["id"]))
        distillery = Distillery(result["name"], result["region"], result["founded"], whiskies)
        distilleries.append(distillery)
    return distilleries

def select(id):
    sql = "SELECT * FROM distilleries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    whiskies = []
    for whisky in result.whiskies:
        whiskies.append(whisky_repository.select(result["id"]))
    distillery = Distillery(result["name"], result["region"], result["founded"], whiskies)
    return distillery

# UPDATE
def update(distillery):
    sql = "UPDATE distilleries SET (name, region, founded, whiskies) = (%s, %s, %s, %s) WHERE id = %s"
    values = [distillery.name, distillery.region, distillery.founded, distillery.whiskies]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM distilleries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM distilleries WHERE id = %s"
    values = [id]
    run_sql(sql, values)
