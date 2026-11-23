from fastapi import FastAPI


gawab = FastAPI()
items = []
@gawab.get("/")
def root():  
    return {"message": "Hello World"}

@gawab.post("/items")
def create_item(item: str):
    items.append(item)
    return {"added": item, "items": items}

@gawab.get("/items")
def list_items():
    return items   
