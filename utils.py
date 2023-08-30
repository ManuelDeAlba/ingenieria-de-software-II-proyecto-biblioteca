import pandas as pd

# Funciones para manejar la información en el csv
def guardarDatosCSV(datos, archivo):
	df = pd.DataFrame(datos) # Se crea el data frame que se va a guardar

	# Se guarda la informacion
	df.to_csv(archivo, index=False) # No nos interesa guardar los indices en el archivo

def leerDatosCSV(archivo):
	try:
		df2 = pd.read_csv(archivo) # header=None, skiprows=1, names=["uno","dos","tres"]
		dict = df2.to_dict(orient="split") # Se convierte en diccionario para leerlo más fácil

		return dict["data"]
	except:
		# Manejo de errores por si no hay datos o el archivo no existe
		return False