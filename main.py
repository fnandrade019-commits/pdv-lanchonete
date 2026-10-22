from fastapi import FastAPI
app = FastAPI()

cardapio = [
    
    {"nome": "X-Burger", "categoria": "Lanches", "preco":25.00 },
    {"nome": "Bolo Confeitado", "categoria": "Lanches", "preco":5.00},
    {"nome": "Coca Cola", "categoria": "Bebidas", "preco":6.00}
    
    ]

@app.get("/produtos")
def listar_produtos ():
    return cardapio

print (listar_produtos())
