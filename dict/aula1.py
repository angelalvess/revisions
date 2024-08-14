person = {
    "name": "John",
    "age": 36,
    "country": "Norway",
    "address": [
         {
            "street": "Main St",
            "number": 123,
            "city": "Springfield",
            "state": "IL",
            "zip": 62701
         },
        {
            "street": "Broadway",
            "number": 456,
            "city": "Springfield",
            "state": "IL",
            "zip": 62701
         }
    ]
}

for key in person:
    print(key, person[key])
