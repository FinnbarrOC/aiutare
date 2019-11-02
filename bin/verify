#!/usr/bin/env python3
import os
import mongoengine
from mongoengine.context_managers import switch_db
import shutil
from multiprocessing import Process
from categories.smt.config import config as og_config  # TODO: should be accessing bin.benching.config instead
from bin.verification.v_config import config as v_config
from categories.smt.schemas import Result, Instance
from bin.mongod_manager import write_config, start_server, end_server
from bin.benching.run import run
from pathlib import Path


def parse_models(models):
    models_arr = models.replace('\n', '').split("(model")[1:]
    assertions = []

    for model in models_arr:
        model = model[0:-1]

        lines = model.split("(define-fun ")[1:]
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            var_name = lines[i][0:lines[i].find(' ')]
            var_value = lines[i][lines[i].rfind(' '):-1]
            lines[i] = "(assert (= " + var_name + " " + var_value + "))"

        assertions.append("\n" + '\n'.join(lines) + "\n")

    return assertions


def insert_statements(new_filename, assertions):
    with open(new_filename, 'r+') as v_inst:

        lines = v_inst.readlines()
        cur_check_sat = 0
        for i in range(len(lines)):
            if "(check-sat)" in lines[i]:
                try:
                    lines[i] = assertions[cur_check_sat] + "\n" + lines[i]
                    cur_check_sat += 1
                except IndexError:
                    lines[i] = assertions[-1] + "\n" + lines[i]

        v_inst.seek(0)
        v_inst.truncate()
        v_inst.writelines(lines)


def modify_instance(nickname, filename, models):
    new_dir = v_config["instances"] + "/" + nickname + "/" + filename.rsplit(os.sep, 1)[0]
    new_filename = v_config["instances"] + "/" + nickname + "/" + filename

    os.makedirs(new_dir, exist_ok=True)
    shutil.copy(filename, new_filename)

    assertions = parse_models(models)
    insert_statements(new_filename, assertions)


# Populate bin/verification/v_instances with new instances
# created by inserting solvers' models into original instances
def generate_v_instances():
    mongoengine.connect(og_config["database_name"], alias="default", replicaset="monitoring_replSet")

    # Clear the v_instances directory for each program run
    shutil.rmtree(v_config["instances"], ignore_errors=True)
    os.mkdir(v_config["instances"])

    for sat_result in Result.objects():
        if sat_result.result == "sat":
            modify_instance(sat_result.nickname, sat_result.instance.filename, sat_result.model)

    mongoengine.connection.disconnect()


def drop_v_db():
    v_db = mongoengine.connect(v_config["database_name"], alias=v_config["database_name"],
                               replicaset="monitoring_replSet")
    v_db.drop_database(v_config["database_name"])
    v_db.close()


def evaluate_models():
    mongoengine.connect(v_config["database_name"], alias=v_config["database_name"], replicaset="monitoring_replSet")

    good_models = []
    bad_models = []

    # NOTE: this switch_db call is needed to access Instances from the (non-default) verification database
    with switch_db(Instance, v_config["database_name"]) as v_Instance:
        for v_instance in v_Instance.objects():
            identification = v_instance.filename[len(v_config["instances"]) + 1:].split(os.sep, 1)
            nickname = identification[0]
            instance_filename = Path(identification[1])  # Users should relative filepath for instance directory

            # This model is "verified" sat by all solvers
            if v_instance.num_unsat == 0:
                good_models.append((nickname, instance_filename))

            # Otherwise, some solver did not find this model to be sat
            else:
                bad_models.append((nickname, instance_filename))

    mongoengine.connection.disconnect()

    return good_models, bad_models


def update_results(good_models, bad_models):
    mongoengine.connect(og_config["database_name"], alias="default", replicaset="monitoring_replSet")

    verified_instances = []

    # First loop checks all sat results using data from model verification
    print("\nFalsified Models:")
    print("-----------------")
    for sat_result in Result.objects(result="sat"):
        if (sat_result.nickname, Path(sat_result.instance.filename)) in good_models:
            sat_result.modify(set__verified="YES")
            verified_instances.append(sat_result.instance.filename)

        elif (sat_result.nickname, Path(sat_result.instance.filename)) in bad_models:
            sat_result.modify(set__verified="NO")
            print(sat_result.nickname, sat_result.instance.filename)

    for verified_instance in Instance.objects():
        if verified_instance.filename in verified_instances:
            verified_instance.modify(set__verified_sat=True)

    # Second loop checks all unsat results compared against new model data
    print("\nFalsified Unsats:")
    print("-----------------")
    for unsat_result in Result.objects(result="unsat"):
        if unsat_result.instance.verified_sat is False:
            unsat_result.modify(set__verified="YES")

        elif unsat_result.instance.verified_sat is True:
            unsat_result.modify(set__verified="NO")
            print(unsat_result.nickname, unsat_result.instance.filename)

    mongoengine.connection.disconnect()


def main():
    write_config("bin/verification/v_config.py")
    start_server()

    mongoengine.register_connection("default", og_config["database_name"], og_config["database_name"])
    mongoengine.register_connection(v_config["database_name"], v_config["database_name"], v_config["database_name"])

    instance_generator = Process(target=generate_v_instances)
    v_db_dropper = Process(target=drop_v_db)
    instance_generator.start()
    v_db_dropper.start()
    instance_generator.join()
    v_db_dropper.join()

    runner = Process(target=run, args=[1])
    runner.start()
    runner.join()

    good_models, bad_models = evaluate_models()
    update_results(good_models, bad_models)

    kill_server = False  # TODO: handle with argparse
    if kill_server:
        end_server()


if __name__ == '__main__':
    main()
