import pdb
from db.run_sql import run_sql
from models.whisky import Whisky
from models.distillery import Distillery
import repositories.distillery_repository as distillery_repository

# CREATE
# define function to save a whisky
def save(whisky):
    # sql query = create entry in whiskies table using values given below, returning the created row in the table
    sql = "INSERT INTO whiskies (name, type, flavour_profile, distillery_id) VALUES (%s, %s, %s, %s) RETURNING * "
    # set distillery id to None
    distillery_id = None
    # if whisky's distillery is not equal to None
    if whisky.distillery != None:
        # set distillery_id to the whisky's distillery's
        distillery_id = whisky.distillery.id
    # set values to pass into sql query as whisky name, whisky type, whisky flavour profile and distillery_id
    values = [whisky.name, whisky.type, whisky.flavour_profile, distillery_id]
    # run the run_sql function passing in the sql query and values and return the results to the results variable
    results = run_sql(sql, values)
    # set id to equal the value associated with the id key of the 0th index of the results
    id = results[0]["id"]
    # set the whisky's id to be equal to id
    whisky.id = id
    # return whisky
    return whisky

# READ
def select_all():
    whiskies = []
    sql = "SELECT * FROM whiskies"
    results = run_sql(sql)
    for result in results:
        distillery = None
        if result["distillery_id"] != None:
            distillery = distillery_repository.select(result["distillery_id"])
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"], distillery, result["id"])
        whiskies.append(whisky)
    return whiskies

def select(id):
    sql = "SELECT * FROM whiskies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    whisky = None
    if result["distillery_id"] != None:
        distillery_id = result["distillery_id"]
        distillery = distillery_repository.select(distillery_id)
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"], distillery, result["id"])
    else:
        whisky = Whisky(result["name"], result["type"], result["flavour_profile"], None, result["id"])
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
    results = run_sql(sql, values)[0]
    whiskies = []
    distillery = Distillery(results["name"], results["region"], results["founded"], whiskies, results["id"])
    return distillery

def select_by_distillery(distillery_id):
    whiskies = []
    sql = "SELECT * FROM whiskies where distillery_id = %s"
    values = [distillery_id]
    results = run_sql(sql, values)
    for result in results:
        whiskies.append(result)
    return whiskies

