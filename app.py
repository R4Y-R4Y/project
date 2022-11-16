from flask import Flask, request
from db import stores
import uuid
import sys
app = Flask(__name__)


@app.get("/stores")

def get_stores():
    return{"stores": stores}

@app.get("/stores/<int:id>")

def get_store(id):
    for x in stores:
        # if you want to print log in the terminal try this
        print(x, file=sys.stderr)
        if(x['id'] == id):
            return({"store":x})
    return {"Message":"Store with id "+ str(id) +" not Found"},404

@app.post("/stores")

def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"],"id":uuid.uuid4().hex, "items":[]}
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


