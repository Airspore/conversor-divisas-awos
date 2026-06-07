from fastapi import FastAPI

app = FastAPI(title="Web Service de Divisas - Actividad 2")

# Tasas de cambio aproximadas (puedes ajustarlas si lo deseas)
TASA_EURO_MXN = 18.50
TASA_USD_MXN = 17.00
TASA_CAD_MXN = 12.50
TASA_LIBRA_MXN = 21.50

# 1. Euro a Pesos MX
@app.get("/euro-a-mxn/{cantidad}")
def euro_a_mxn(cantidad: float):
    resultado = cantidad * TASA_EURO_MXN
    return {"moneda_origen": "Euro", "cantidad": cantidad, "moneda_destino": "MXN", "resultado": resultado}

# 2. Dólar US a Pesos MX
@app.get("/usd-a-mxn/{cantidad}")
def usd_a_mxn(cantidad: float):
    resultado = cantidad * TASA_USD_MXN
    return {"moneda_origen": "USD", "cantidad": cantidad, "moneda_destino": "MXN", "resultado": resultado}

# 3. Dólar Canadiense a Pesos MX
@app.get("/cad-a-mxn/{cantidad}")
def cad_a_mxn(cantidad: float):
    resultado = cantidad * TASA_CAD_MXN
    return {"moneda_origen": "CAD", "cantidad": cantidad, "moneda_destino": "MXN", "resultado": resultado}

# 4. Libra a Pesos MX
@app.get("/libra-a-mxn/{cantidad}")
def libra_a_mxn(cantidad: float):
    resultado = cantidad * TASA_LIBRA_MXN
    return {"moneda_origen": "Libra", "cantidad": cantidad, "moneda_destino": "MXN", "resultado": resultado}

# 5. Pesos MX a Euro
@app.get("/mxn-a-euro/{cantidad}")
def mxn_a_euro(cantidad: float):
    resultado = cantidad / TASA_EURO_MXN
    return {"moneda_origen": "MXN", "cantidad": cantidad, "moneda_destino": "Euro", "resultado": resultado}

# 6. Pesos MX a Dólar US
@app.get("/mxn-a-usd/{cantidad}")
def mxn_a_usd(cantidad: float):
    resultado = cantidad / TASA_USD_MXN
    return {"moneda_origen": "MXN", "cantidad": cantidad, "moneda_destino": "USD", "resultado": resultado}

# 7. Pesos MX a Dólar Canadiense
@app.get("/mxn-a-cad/{cantidad}")
def mxn_a_cad(cantidad: float):
    resultado = cantidad / TASA_CAD_MXN
    return {"moneda_origen": "MXN", "cantidad": cantidad, "moneda_destino": "CAD", "resultado": resultado}

# 8. Pesos MX a Libra
@app.get("/mxn-a-libra/{cantidad}")
def mxn_a_libra(cantidad: float):
    resultado = cantidad / TASA_LIBRA_MXN
    return {"moneda_origen": "MXN", "cantidad": cantidad, "moneda_destino": "Libra", "resultado": resultado}