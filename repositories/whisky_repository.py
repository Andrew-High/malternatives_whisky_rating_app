import pdb
from db.run_sql import run_sql
from models.whisky import Whisky
import repositories.distillery_repository as distillery_repository

# CREATE
def save(whisky):
    sql = "INSERT INTO whiskies (name, type, flavour_profile, distillery_id) VALUES (%s, %s, %s, %s) RETURNING * "
    distillery_id = None
    if whisky.distillery != None:
        # pdb.set_trace()
        distillery_id = whisky.distillery.id
    values = [whisky.name, whisky.type, whisky.flavour_profile, distillery_id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    whisky.id = id
    return whisky

# READ
def select_all():
    whiskies = []
    sql = "SELECT * FROM whiskies"
    results = run_sql(sql)
    for result in results:
        distillery = None
        # pdb.set_trace()
        if result["distillery_id"] != None:
            distillery = distillery_repository.select(result["distillery_id"])
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"], distillery)
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

# additional logic functions
def get_distillery(distillery_id):
    sql = "SELECT * FROM distilleries WHERE id = %s"
    values = [distillery_id]
    results = run_sql(sql, values)
    distillery = Distillery(results["name"], results["region"], results["founded"], results["id"])
    return distillery

