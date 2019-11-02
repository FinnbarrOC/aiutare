#!/usr/bin/env python3
import glob
import sys
import progressbar
import importlib.util
from pymongo import MongoClient
from multiprocessing import Process
import bin.benching.config as config_file
from bin.benching.error_file_writer import read_num_errors, create_error_file


def collect_handlers():
    handlers = {}

    for program in config_file.config["handlers"].items():
        cur_module = importlib.import_module(program[1])
        handlers[program[0]] = cur_module.output_handler

    return handlers


def monitor_database(num_instances, num_bench):
    commands = config_file.config["commands"]

    num_commands = 0
    for program in list(commands.values()):
        num_commands += len(list(program.values()))

    print("Running %d total commands\n" % (num_commands * num_instances * num_bench))

    client = MongoClient()
    db = client[config_file.config["database_name"]]

    with db.watch([{'$match': {'operationType': 'insert'}}]) as stream:

        for _ in progressbar.progressbar(range(num_commands * num_instances * num_bench)):
            stream.next()
            # print(stream.next()["fullDocument"])  TODO: possibly use for live-updating output


def run(num_bench):
    importlib.reload(config_file)
    if num_bench > 0:

        create_error_file()

        instances = glob.glob("%s/**/*.%s" % (config_file.config["instances"], config_file.config["file_extension"]),
                              recursive=True)

        schemas = importlib.import_module(config_file.config["schemas"])
        instance_writer = Process(target=schemas.write_instances, args=[instances])
        instance_writer.start()
        handlers = collect_handlers()
        instance_writer.join()

        database_monitor = Process(target=monitor_database, args=(len(instances), num_bench))
        database_monitor.start()

        from bin.benching.bench import bench
        for _ in range(0, num_bench):
            try:
                bench(instances, handlers)
            except Exception as e:
                print("KILLING BENCHMARKING: ", e, file=sys.stderr)

        database_monitor.join()
        database_monitor.terminate()

        read_num_errors()
