config = {'file_extension': 'smt2', 'commands': {'z3': {'z3_seq': 'categories/smt/tools/z3_federico smt.string_solver=seq -T:33 dump_models=true', 'z3_federico': 'categories/smt/tools/z3_federico smt.string_solver=z3str3 -T:33 dump_models=true', 'z3_master': 'categories/smt/tools/z3_master smt.string_solver=z3str3 -T:33 dump_models=true'}, 'cvc4': {'cvc4_models': 'categories/smt/tools/cvc4 --lang smt --strings-exp --tlimit=33000 -q --dump-models'}}, 'timeout': 30.0, 'handlers': {'z3': 'categories.smt.z3_handler', 'cvc4': 'categories.smt.cvc4_handler'}, 'database_name': 'smt_verification', 'schemas': 'categories.smt.schemas', 'instances': 'bin/verification/v_instances'}
