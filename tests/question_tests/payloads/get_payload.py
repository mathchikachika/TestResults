import inspect, os, sys, json

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
def get_payload_data() -> str:
    payload_file_name = CURRENT_DIR + '\\' + inspect.stack()[1].function + '.json'
    try:
        with open(payload_file_name, 'r') as payload_file:
            payload_data = payload_file.read()
            return str(payload_data)
    except FileNotFoundError as e:
        print(str(e))
    return "-1"
    
