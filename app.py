from flask import Flask, request
app = Flask(__name__)
stores = [
    {
        "name": "Big Store",
        "id": 0,
        "items": [
            {
                "id":1,
                "name": "milk",
                "price": 0.69
            },
        ]
    }
]

@app.get("/stores")

def get_stores():
    return{"stores": stores}

@app.post("/stores")

def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"],"id":len(stores), "items":[]}
    stores.append(new_store)
    return new_store

@app.post("/stores/<int:id>/item/")

def create_item(id):
    request_data = request.get_json()
    new_item = {"name": request_data["name"],"id":id,"price":request_data['price']}
    index = -1
    b = False
    for x in stores:
        index += 1
        if(x['id'] == id):
            b = True
            break
    print(index)
    if(b != True):
        return {"error":"store not found"},400
    stores[index]["items"].append(new_item)
    return new_item,201


