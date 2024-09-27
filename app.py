from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def api():
    return {"message": "Hello World"}

#Aufgabe 1
#Einfache addition für die umrechnung
@app.get("/tempcel/{celsius}") 
async def celToKel(celsius: float):
    kelvin_add = 273.15
    result = celsius + kelvin_add #addieren der Zahl 275.15 um kelvin zu erhalten
    
    return {
        "celsius": celsius,
        "kelvin": result
    }

@app.get("/tempkel/{kelvin}")
async def kelToCel(kelvin: float):
    celsius_sub = 273.15
    result = kelvin - celsius_sub #subtraktion der Zahl 275.15 um Celsius zu erhalten
    
    return {
        "kelvin": kelvin, 
        "celsius": result        
    }

#Aufgabe 2
@app.get("/prime/{limit}")
async def sieve_of_eratosthenes(limit: int)
    is_prime = [True] * (limit + 1) #erstellt eine Liste welche alle Zahlen auf True setzt
    is_prime[0], is_prime[1] = False, False #0,1 keine prim zahlen also False
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False
    
    return[num for num, prime in enumerate(is_prime) if prime]

#Aufgabe 3
@app.get("/number/{limit}")
async def fib(limit: int, a=0, b=1):
    n = limit
    a, b = 0, 1 #definiert die ersten beiden fibonacci nummern

    for _ in range(1, n+1): #fib wird standartmässig bei 0 angefangen aber hier bei 1 deswegen n+1
        a, b = b, a+b

    return{"limit": limit, "number": a}