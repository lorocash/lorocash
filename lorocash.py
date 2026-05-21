from fastapi import FastAPI, Request, Response

# Inicializa o servidor FastAPI exigido pelo Uvicorn
app = FastAPI()

# Definição básica do objeto do servidor x402
X402Server = "X402_server"

def x402_protected(server, prices, network, pay_to):
    def decorator(func):
        return func
    return decorator

# ==========================================
# CONFIGURAÇÃO DE PAGAMENTO: REDE TRON
# ==========================================
@app.get("/credit")
@x402_protected(
    server=X402Server,
    prices=["1 USDT"],
    network="tron:mainnet",
    pay_to="TPS14N9o1FPeowTQkyymyvwZpcXzrR5AHD"
)
async def recharge_credits(request: Request):
    return {"status": "success", "credit": 1000000}


# ==========================================
# CONFIGURAÇÃO DE PAGAMENTO: REDE BNB CHAIN
# ==========================================
@app.get("/credit")
@x402_protected(
    server=X402Server,
    prices=["1 USDT"],
    network="eip155:56",
    pay_to="0xf209db88a825218f0b8bd3018ef4d72112100e49"
)
async def recharge_credits_bnb(request: Request):
    return {"status": "success", "credit": 1000000}
