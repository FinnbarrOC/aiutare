import os
import importlib
from bin.benching.config import config
from bin.benching.error_file_writer import write_error


# Parses the stdout + stderr output from running the problem
# and extracts useful information
def output_handler(nickname, instance, output, elapsed):
    result = 'error'
    model = None

    try:
        # Basic parsing for SAT and UNSAT
        if 'UNSAT' in output or 'unsat' in output:
            result = 'unsat'
        elif 'SAT' in output or 'sat' in output:
            result = 'sat'
        elif 'TIMEOUT' in output or 'timeout' in output:
            result = 'timeout'
        elif 'UNKNOWN' in output or 'unknown' in output:
            result = 'unknown'

        # Advanced parsing for feature extraction
        if result == "sat":
            model = output.split('\n', 1)[1]

    # Catches any errors in the user-made parsing above
    except Exception as e:

        write_error(nickname, instance, str(e))

    # Passes off info to the schemas file to be written to the database
    finally:
        schemas = importlib.import_module(config["schemas"])
        schemas.write_results(os.path.basename(__file__).rsplit("_", 1)[0],
                              nickname, instance, result, elapsed, model)
