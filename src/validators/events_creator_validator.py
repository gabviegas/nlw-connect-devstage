from cerberus import Validator

def events_creator_validator(request: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name" : { "type": "string", "required": True, "empty": False }
            }
        }
    })

    response = body_validator.validate(request.json)

    if response == False:
        print(body_validator.errors) # printa o erro que o validador pegou