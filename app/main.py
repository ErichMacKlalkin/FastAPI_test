from fastapi import FastAPI
import uvicorn
from entity_db import database, entities
from models import Entity, EntityIn, EntityInPartial
from typing import List

app = FastAPI()


# DataBase Connection
@app.on_event("startup")
async def startup():
    await database.connect()


# DataBase Disconnection
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Handlers


# Get document by ID
@app.get("/entities/{entityId}", response_model=Entity, tags=["Get_Entity"])
async def get_entity_by_id(id: int):
    query = entities.select().where(entities.c.id == id)
    return await database.fetch_one(query)


# Create a new document entity
@app.post("/entities/", response_model=Entity, tags=["Create_Entity"])
async def create_entity(entity: EntityIn):
    query = entities.insert().values(name=entity.name, date=entity.date, content=entity.content, owner=entity.owner)
    record = await database.execute(query)
    return {**entity.dict(), "id": record}


# Delete an existing document entity
@app.delete("/entities/{entityId}", tags=["Delete_Entity"])
async def delete_entity(id: int):
    query = entities.delete().where(entities.c.id == id)
    await database.execute(query)

    return {
        "status": True,
        "message": "This entity has been deleted successfully."
    }


# A full update of a document entity
@app.put("/entities{entity_id}", response_model=Entity, tags=["Modify_Entity"])
async def update_entity(entity_id: int, entity: EntityIn):
    query = entities.update().where(entities.c.id == entity_id).values(name=entity.name, date=entity.date,
                                                                       content=entity.content, owner=entity.owner)
    await database.execute(query)
    return await get_entity_by_id(entity_id)


# Beside the task requirements. To show all existing documents entities for you convenience.
@app.get("/entities/", response_model=List[Entity], tags=["Get_Entity"])
async def get_all_entities():
    query = entities.select()
    return await database.fetch_all(query)


# A partial update of a document entity
@app.patch("/entities{entity_id}", response_model=Entity, tags=["Modify_Entity"])
async def partial_update_entity(entity_id: int, entity: EntityInPartial):
    query = entities.update().where(entities.c.id == entity_id).values(entity.dict(exclude_none=True))
    await database.execute(query)
    return await get_entity_by_id(entity_id)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
