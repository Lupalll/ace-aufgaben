from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def api():
    return {"message": "Hello from your local FastAPI!"}

#eigentliche aufgabe
@app.get("/tempcel/{celsius}") #eingabe der Zahl für die Umrechung
async def celToKel(celsius: float):
    kelvin_add = 273.15
    result = celsius + kelvin_add #addiere 275.15 erhalte kelvin
    
    return {
        "celsius": celsius,
        "kelvin": result
    }

@app.get("/tempkel/{kelvin}") #eingabe der Zahl für die Umrechung
async def kelToCel(kelvin: float):
    celsius_sub = 273.15
    result = kelvin - celsius_sub #subtrahiere 275.15 erhalte celsius
    
    return {
        "kelvin": kelvin, 
        "celsius": result        
    }



@app.get("/tempkel/{kelvin}") #eingabe der Zahl für die Umrechung
async def kelToCel(kelvin: float):
    celsius_sub = 273.15
    result = kelvin - celsius_sub #subtrahiere 275.15 erhalte celsius
    
    return {
        "kelvin": kelvin, 
        "celsius": result        
    }
