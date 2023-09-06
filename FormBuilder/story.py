JsonSchema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "properties": {
        "first name": {
            "description": "Please provide your first name",
            "type": "string"
        },
        "last name": {
            "description": "Please provide your last name",
            "type": "string"
        },
        "home address": {
            "description": "Please provide your home address",
            "type": "string"
        },
        "work experience": {
            "type": "array",
            "item": {
                "type": "object",
                "properties": {
                    "duration": {
                        "description": "Please provide the duration of this working experience",
                        "type": "string"
                    },
                    "summary": {
                        "description": "Please provide a short summary of this working experience",
                        "type": "string"
                    },
                }
            }
        },
        "phone number": {
            "description": "Please provide your phone number",
            "type": "string"
        },
        "birthday": {
            "description": "Please provide your birthday",
            "type": "string"
        },
    },
}

def getAnswer(key, description, json):
    print(description)
    value = input('input: ')
    json[key] = value

def run(schema, json):
    properties = schema['properties']
    for key, value in properties.items():
        type = value['type']
        if type != 'array':
            getAnswer(key, value['description'], json)
        else:
            json[key] = []
            while True:
                item = value['item']
                child = {}
                run(item, child)
                json[key].append(child)

                nextOne = ''
                while True:
                    nextOne = input('add another item (yes/no): ').upper()
                    if nextOne != 'YES' and nextOne != 'NO':
                        continue
                    break
                if nextOne == 'YES':
                    continue
                break


output = {}
run(JsonSchema, output)
print(output)