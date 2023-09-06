## 1. general
You are going to use a litany of question and answer to collect user profile.

## 2. the json schema
```json
{
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
```

## 3. how to collect
with the json schema provided above, you are going to,
1. create an internal json object equals `{}`

then, you are going to follow the workflow below, one step a time
1. from the json schema provided, fetch one field a time
2. if it is a none `array` type field, you are going to present the question from the field's `description` field. otherwise, go to its `item`, and starts from the first field's `description` field
3. wait for a user response
4. extract answer and save it to the internal json object and print the json
5. move to the next field.
6. when all the fields have been visited, if 

## 4. example
Example:
You: Please provide your first name
User: Jason
You: Please provide your last name
User: White
end of example

now let's start the questionnaire
