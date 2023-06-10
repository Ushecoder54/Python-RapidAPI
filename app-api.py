from fastapi import FastAPI

app = FastAPI()

richest_people_list = {
    "Aliko Dangote": "18,5 Billion",
    "Johann Rupert": "8,71 Billion",
    "Nicky Oppenheimer": "7.93 Billion",
    "Nathan Kirsh": "7.21 Billion",
    "Nassef Sawiris": "6.44 Billion" 
}

@app.get("/richest_people")
def richest_people():
    return richest_people_list