from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List




app = FastAPI(
    title = "API CONCIERTOS",
    description="UNA API DE CONCIERTOS",
    version="1.0.0"
)

class ConcertCreate(BaseModel):
    artists: List[str]
    city: str
    date: str
    sold_out: bool = False

class Concert(ConcertCreate):
    id : int


# -------- FAKE DATABASE (IN MEMORY) --------

concerts_db: List[Concert] = [
    Concert(
        id=1,
        artists=["Coldplay"],
        city="Madrid",
        date="2026-05-10",
        sold_out=True
    ),
    Concert(
        id=2,
        artists=["Metallica"],
        city="Barcelona",
        date="2026-06-01",
        sold_out=False
    ),
    Concert(
        id=3,
        artists=["Dua Lipa"],
        city="Sevilla",
        date="2026-07-15",
        sold_out=False
    ),
    Concert(
        id=4,
        artists=["Arctic Monkeys", "The Hives"],
        city="Valencia",
        date="2026-06-25",
        sold_out=True
    ),
    Concert(
        id=5,
        artists=["Rosalía"],
        city="Madrid",
        date="2026-09-03",
        sold_out=False
    ),
    Concert(
        id=6,
        artists=["Imagine Dragons"],
        city="Lisboa",
        date="2026-08-20",
        sold_out=False
    ),
    Concert(
        id=7,
        artists=["Quevedo", "C. Tangana"],
        city="Sevilla",
        date="2026-05-28",
        sold_out=True
    ),
    Concert(
        id=8,
        artists=["Red Hot Chili Peppers"],
        city="Barcelona",
        date="2026-07-07",
        sold_out=True
    ),
    Concert(
        id=9,
        artists=["Aitana"],
        city="Bilbao",
        date="2026-06-18",
        sold_out=False
    ),
    Concert(
        id=10,
        artists=["Muse"],
        city="Madrid",
        date="2026-10-02",
        sold_out=False
    ),
]

next_id = 11


@app.get("/")
def root():
    return {"message": "La API funciona"}

@app.get("/concerts")
def get_concerts():
    return concerts_db

@app.get("/concerts/{concert_id}")
def get_concert(concert_id: int):
    for concert in concerts_db:
        if concert.id == concert_id:
            return concert
    raise HTTPException(404, detail="Concierto no se encuentra") 


@app.post("concerts", status_code=201)
def crear_concierto(concert_data: ConcertCreate):
    global next_id

    new_concert = Concert(
        id = next_id,
        artists=concert_data.artists,
        city=concert_data.city,
        date=concert_data.date,
        sold_out=concert_data.sold_out
    )

    concerts_db.append(new_concert)
    next_id += 1
    return new_concert

@app.put("/concerts/{concert_id}")
def update_concert(concert_id: int, concert_data: ConcertCreate):
    for concert in concerts_db:
        if concert.id == concert_id:
            concert.artists = concert_data.artists
            concert.city = concert_data.city
            concert.date = concert_data.date
            concert.sold_out = concert_data.sold_out
            return concert

    raise HTTPException(404, detail="Concierto no se encuentra")

@app.delete("/concerts/{concert_id}", status_code=204)
def delete_concert(concert_id: int):
    for concert in concerts_db:
        if concert.id == concert_id:
            concerts_db.remove(concert)
            return

    raise HTTPException(404, detail="Concierto no se encuentra")

@app.get("/concerts/city/{city}")
def get_concerts_by_city(city: str):
    concerts_city = []
    for concert in concerts_db:
        if concert.city.lower() == city.lower():
            concerts_city.append(concert)
    return concerts_city

@app.get("/concerts/artist/{artist}")
def get_concerts_by_artist(artist: str):
    concerts_artist = []
    for concert in concerts_db:
        if any(a.lower() == artist.lower() for a in concert.artists):
            concerts_artist.append(concert)
    return concerts_artist

@app.get("/concerts/sold_out/{status}")
def get_concerts_by_sold_out_status(status: bool):
    concerts_status = []
    for concert in concerts_db:
        if concert.sold_out == status:
            concerts_status.append(concert)
    return concerts_status
