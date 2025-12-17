import json
import math
import urllib3
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta

ruta_database = 'database.json'
app = FastAPI()

def listar_datos():
    try:
        with open(ruta_database, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except json.JSONDecodeError:
        print("JSON inválido.")

def respalda_datos():
    try:
        with open(ruta_database, 'w') as archivo:
            datos = json.dumps(archivo)
        return datos
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except json.JSONDecodeError:
        print("JSON inválido.")

async def get_indice_dolar(fecha):
    url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@" + fecha + "/v1/currencies/usd.json"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = json.loads(response.data.decode('utf-8'))
    return data["usd"]["ars"]

# Valida el id y devuelve los datos de la receta normalizados
async def valida_receta(id_receta):
	datos = listar_datos()
	recetaID = ''
	nombre_receta = ''
	precio_pesos = 0
	receta = ''

	# Valida el ID, guarda el nombre y el objeto receta
	for item in datos["Recetas"]:
		if item.get("id") == 1:
			recetaID = item.get("id")
			nombre_receta = item.get("receta")
			receta = item
			break

	# Normaliza los datos de la receta
	for item_receta in receta["Lista de Ingredientes"]:
		# Ajusta a 250 grs
		if item_receta["peso"] % 250 != 0:
			item_receta["peso"] = math.ceil(item_receta["peso"] / 250) * 250
			# convierte grs a kilos
			nuevo_peso = (item_receta["peso"] / 1000)
			item_receta["peso"] = nuevo_peso
		# calcula el precio total de la receta
		for item_ingrediente in datos["Ingredientes"]:
			if item_receta["ingrediente"] == item_ingrediente["ingrediente"]:
				precio_pesos = (item_receta["peso"] * item_ingrediente["precio"]) + precio_pesos

	return recetaID, nombre_receta, precio_pesos

# Valida y respalda el pedido
async def valida_pedido(id_receta, pedido_fecha, cotizar_fecha):
	respuesta = ''
	datos = listar_datos()
	for item in datos["Recetas"]:
		if item.get("id") == 1:
			recetaID = item.get("id")
			nombre_receta = item.get("receta")
		else:
			respuesta = {'Id de receta inválido'}

	nuevo_pedido = {
		"id_receta" : id_receta,
		"pedido_fecha" : pedido_fecha,
		"cotizar_fecha" : cotizar_fecha
	}
	
	data['Pedidos'].append(nuevo_pedido)

	respalda_datos()
	
	if not respuesta:
		respuesta = nuevo_pedido

	return respuesta

@app.get('/api/recetas')
async def recetas():
    datos = listar_datos()
    return json.dumps(datos["Recetas"])

@app.get('/api/cotizar')
async def cotizar(id_receta: int, cotiza_fecha: str ):
	recetaID, nombre_receta, precio_pesos = await valida_receta(id_receta)

	# Valida fecha
	formato = '%Y-%m-%d'
	try:
		fecha = datetime.strptime(cotiza_fecha, formato)
	except ValueError:
		return jsonify({"error":"Formato de fecha inválido"}), 400

	fecha_actual = datetime.now()
	fecha_limite = fecha_actual - timedelta(days=30)
	if fecha < fecha_limite and fecha > fecha_actual:
		return jsonify({"error":"Fecha inválida"}), 400

	indice_dolar = await get_indice_dolar(cotiza_fecha)
	precio_dolar = precio_pesos * indice_dolar

	return {"ID": recetaID, "fecha": nombre_receta, "$": precio_pesos, "US$": precio_dolar}

@app.get('/api/pedido')
async def pedido(id_receta: int, pedido_fecha: str, cotiza_fecha: str ):
		respuesta = await valida_pedido(id_receta, pedido_fecha, cotiza_fecha)

		return respuesta
