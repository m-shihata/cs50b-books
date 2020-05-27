from flask import request

def get(input_name):
    if request.form.get(input_name):
        return request.form.get(input_name)
    return None
