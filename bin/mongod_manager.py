#!/usr/bin/env python3

import time
import psutil
import platform
import importlib.util
from pymongo import MongoClient
from subprocess import Popen, DEVNULL


def write_config(config_filepath):

    spec = importlib.util.spec_from_file_location("config", config_filepath)
    config_file = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_file)
    config = config_file.config

    # Converts modules into importable format
    config["schemas"] = config["schemas"].rsplit(".", 1)[0].replace("/", ".")
    for program, handler in config["handlers"].items():
        config["handlers"][program] = handler.rsplit(".", 1)[0].replace("/", ".")

    # Writes a local copy of the user-provided config file
    with open("bin/benching/config.py", "w") as file:
        file.write("config = " + str(config) + "\n")
        file.flush()


# Waits until the server is accepting connections before returning
def ping_server():
    client = MongoClient()
    while client.local.command('ping')['ok'] != 1.0:
        time.sleep(0.5)


def start_server():
    # Checks if a server is already running
    for process in psutil.process_iter():
        if process.name() == "mongod" or process.name() == "mongod.exe":
            return

    if platform.system() == "Windows":
        mongod_location = input("Please input the location of your mongod executable: ")

        print("Starting new mongod server process")
        Popen("\"%s\" " % mongod_location +
              "--dbpath=\"./results\" " +
              "--logpath=\"./results/log/mongodb.log\" " +
              "--replSet=\"monitoring_replSet\" ")

        ping_server()

        Popen([(mongod_location.replace("mongod.exe", "mongo.exe")), "--eval", "\"rs.initiate()\""], stdout=DEVNULL)

    else:
        print("Starting new mongod server process")
        Popen(["mongod", "--dbpath", r"./results", "--logpath", r"./results/log/mongodb.log",
               "--replSet", "monitoring_replSet"], stdout=DEVNULL)

        ping_server()

        Popen(["mongo", "--eval", "rs.initiate()"], stdout=DEVNULL)


def end_server():
    for process in psutil.process_iter():
        if process.name() == "mongod" or process.name() == "mongod.exe":
            process.kill()
