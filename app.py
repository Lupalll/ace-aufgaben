from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def api():
    return {"message": "Hello World"}

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


#zahl hat divisor der kleiner oder gleich quadratwurzel der zahl entspricht
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): #itteriert durch alle zahlen i von 2 bis zur quadratwurzel von num
        if num % i == 0:
            return False
    return True

@app.get("/prime/{limit}")
async def sieve_of_eratosthenes(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False
    
    return[num for num, prime in enumerate(is_prime) if prime]


@app.get("/number/{limit}")
async def fib(limit: int, a=0, b=1):
    n = limit
    a, b = 0, 1 #beiden ersten fib nummern

    for _ in range(1, n+1): #fib wird stdrt bei 0 angefangen aber hier bei 1 deswegen +1
        a, b = b, a+b

    return{"limit": limit, "number": a}
