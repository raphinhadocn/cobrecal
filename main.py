from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI(title="CobreCal")
 
 
# ==============================
# DADOS DA CALCULADORA
# ==============================
 
BITOLAS = {
    "1/4": 0.130,
    "3/8": 0.203,
    "1/2": 0.283,
    "5/8": 0.350,
    "3/4": 0.423,
    "7/8": 0.509
}
 
ADICIONAL = 0.300
 
 
# ==============================
# DADOS RECEBIDOS
# ==============================
 
class Calculo(BaseModel):
    bitola: str
    quantidade: float
    conversao: str
 
 
# ==============================
# ROTA PRINCIPAL
# ==============================
 
@app.get("/")
def inicio():
    return {
        "app": "CobreCal",
        "status": "online"
    }
 
 
# ==============================
# CALCULADORA
# ==============================
 
@app.post("/calcular")
def calcular(dados: Calculo):
 
    # Verifica se a bitola existe
    if dados.bitola not in BITOLAS:
        return {
            "erro": "Bitola inválida."
        }
 
    # Verifica quantidade
    if dados.quantidade < 0:
        return {
            "erro": "A quantidade não pode ser negativa."
        }
 
    peso_por_metro = BITOLAS[dados.bitola]
 
 
    # ==========================
    # KG → METROS
    # ==========================
 
    if dados.conversao == "kg_metros":
 
        metros = dados.quantidade / peso_por_metro
 
        return {
            "conversao": "kg_metros",
            "bitola": dados.bitola,
            "peso": dados.quantidade,
            "metros": round(metros, 2)
        }
 
 
    # ==========================
    # METROS → KG
    # ==========================
 
    elif dados.conversao == "metros_kg":
 
        peso_exato = dados.quantidade * peso_por_metro
 
        peso_com_adicional = peso_exato + ADICIONAL
 
        return {
            "conversao": "metros_kg",
            "bitola": dados.bitola,
            "metros": dados.quantidade,
            "peso_exato": round(peso_exato, 3),
            "peso_com_adicional": round(peso_com_adicional, 3)
        }
 
 
    # ==========================
    # CONVERSÃO INVÁLIDA
    # ==========================
 
    return {
        "erro": "Tipo de conversão inválido."
    }