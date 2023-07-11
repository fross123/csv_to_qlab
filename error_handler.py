errors = []
success = []

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