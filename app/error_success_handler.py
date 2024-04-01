errors = []
success = []
previous_cue_id = ["Fou"]


def handle_errors(status, message):
    print("There was an error:")
    print(message)
    errors.append({"status": status, "message": message})


def return_errors():
    return errors


def count_success(status, message):
    success.append({"status": status, "message": message})


def return_success():
    return success

def clear_errors_and_success():
    errors.clear()
    success.clear()

def store_cue_id(cue_id):
    previous_cue_id.append(cue_id)

def retrieve_previous_cue_id():
    return previous_cue_id[-1]