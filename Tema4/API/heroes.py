from fastapi import FastAPI


app = FastAPI(
    title="Superheroes API (simple)",
    description="Very simple REST API with in-memory data",
    version="1.0.0"
)

from pydantic import BaseModel
from typing import List

class HeroCreate(BaseModel):
    name: str
    power: str
    universe: str
    alive: bool = True

class Hero(HeroCreate):
    id: int

heroes_db: List[Hero] = [
    Hero(id=1, name="Spider-Man", power="Spider-sense", universe="Marvel", alive=True),
    Hero(id=2, name="Batman", power="Intelligence and gadgets", universe="DC", alive=True),
    Hero(id=3, name="Wonder Woman", power="Super strength", universe="DC", alive=True),
    Hero(id=4, name="Iron Man", power="Powered armor", universe="Marvel", alive=False),
    Hero(id=5, name="Thor", power="God of Thunder", universe="Marvel", alive=True),
]

next_id = 6



@app.get("/")
def root():
    return {"message": "Superheroes API is running"}


@app.get("/heroes")
def get_heroes():
    return heroes_db


from fastapi import HTTPException

@app.get("/heroes/{hero_id}")
def get_hero(hero_id: int):
    for hero in heroes_db:
        if hero.id == hero_id:
            return hero
    raise HTTPException(status_code=404, detail="Hero not found")


@app.post("/heroes", status_code=201)
def create_hero(hero_data: HeroCreate):
    global next_id

    new_hero = Hero(
        id=next_id,
        name=hero_data.name,
        power=hero_data.power,
        universe=hero_data.universe,
        alive=hero_data.alive
    )

    heroes_db.append(new_hero)
    next_id += 1

    return new_hero


@app.put("/heroes/{hero_id}")
def update_hero(hero_id: int, hero_data: HeroCreate):
    for hero in heroes_db:
        if hero.id == hero_id:
            hero.name = hero_data.name
            hero.power = hero_data.power
            hero.universe = hero_data.universe
            hero.alive = hero_data.alive
            return hero

    raise HTTPException(status_code=404, detail="Hero not found")


@app.delete("/heroes/{hero_id}", status_code=204)
def delete_hero(hero_id: int):
    for hero in heroes_db:
        if hero.id == hero_id:
            heroes_db.remove(hero)
            return

    raise HTTPException(status_code=404, detail="Hero not found")



