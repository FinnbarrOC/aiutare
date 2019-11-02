import mongoengine
from mongoengine import *
from importlib import reload
import bin.benching.config as config_file


# MongoEngine schemas:
# ---------------------

class Instance(Document):
    filename = StringField(required=True)
    num_sat = IntField(default=0)
    num_unsat = IntField(default=0)
    num_unknown = IntField(default=0)
    verified_sat = BooleanField(default=False)
    # If a solver returns a model for this Instance which ALL solvers find to be "sat",
    # then we assume that this Instance is proven "sat"

    meta = {
        'indexes': [
            {'fields': ['filename'], 'unique': True}
        ]
    }


class Result(Document):
    program = StringField(required=True)
    nickname = StringField(required=True)
    instance = ReferenceField(Instance, required=True)
    result = StringField(required=True)
    elapsed = FloatField(required=True)
    model = StringField()
    verified = StringField(choices=("YES", "NO", "N/A"))
    # YES means that "result" has been verified (if "sat") or not yet disproved (if "unsat")
    # NO means that "result" has been disproved
    # N/A means that the model has not been verified or disproved yet


# Formats and writes results to the database:
# ------------------------------------------------
def write_instances(instances):
    reload(config_file)
    mongoengine.connect(config_file.config["database_name"], replicaset="monitoring_replSet")

    for instance in instances:
        if not Instance.objects(filename=instance):

            Instance.objects(filename=instance). \
                update_one(upsert=True,
                           set__filename=instance)

    mongoengine.connection.disconnect()


# Formats and writes results to the database:
# ------------------------------------------------
def write_results(program, nickname, instance, result, elapsed, model):
    reload(config_file)
    mongoengine.connect(config_file.config["database_name"], replicaset="monitoring_replSet")

    this_instance = Instance.objects.get(filename=instance)

    this_result = Result(program=program)
    this_result.nickname = nickname
    this_result.instance = this_instance
    this_result.result = result
    this_result.elapsed = elapsed

    # For model verification
    if model:
        this_result.model = model
    this_result.verified = "N/A"

    this_result.save(force_insert=True)

    # Updates the current instance's counters with each result
    if result == 'sat':
        this_instance.modify(inc__num_sat=1)
    elif result == 'unsat':
        this_instance.modify(inc__num_unsat=1)
    else:
        this_instance.modify(inc__num_unknown=1)

    mongoengine.connection.disconnect()
