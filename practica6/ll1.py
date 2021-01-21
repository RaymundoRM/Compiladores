from prettytable import PrettyTable
import pandas as pd
import texttable as tt

class ll1:
	def __init__(self,archivo):
		gramatica=self.cargarDesde(archivo)
		self.conjuntoPrimeros=[]
		self.conjuntoSiguiente=[]
		self.terminales=[]
		self.noTerminales=[]
		self.obtenerTerminales(gramatica)
		self.obtenerNoTerminales(gramatica)
		self.obtenerPrimeros(gramatica)
		self.construirTabla()	
		
	def cargarDesde(self,documento):
		listaSaltos=[]
		listaLimpia=[]
		#inicia la lectura del archivo
		with open(documento) as automata:
			for linea in automata:
				listaSaltos.append(linea)
		for i in listaSaltos:#limpiamos los saltos de linea y los asignamos a una lista limpia
			listaLimpia.append((i.rstrip()))
		return(listaLimpia)

	def obtenerTerminales(self,gramatica):
		self.terminales.append(" ")
		for produccion in gramatica:
			for letra in produccion[3:]:
				if letra.islower() and letra not in self.terminales:
					self.terminales.append(letra)
		self.terminales.append("$")

	def obtenerNoTerminales(self, gramatica):
		for produccion in gramatica:
			if produccion[0] not in self.noTerminales:
				self.noTerminales.append(produccion[0])

	def obtenerPrimeros(self, gramatica):	
		primeros=[]	
		pendientes=[]
		vueltas=0
		for produccion in gramatica:
			elementoIzq=produccion[0]
			elementoDer=produccion[3]
			if elementoDer.islower(): #todo en minisculas
				primeros.append(elementoIzq+","+elementoDer)
			else:
				pendientes.append(elementoIzq+","+elementoDer)
		while vueltas <= len(pendientes):
			for j in pendientes:
				for k in primeros:
					if j[2]==k[0]: 	
						primeros.append(j[0]+","+k[2])		
						vueltas+=1
		self.conjuntoPrimeros=pd.unique(primeros)
		print(self.conjuntoPrimeros)

	def construirTabla(self):
		filas=[]
		for i in self.noTerminales:
			for j in self.terminales[1:]:	
				letra=[]
				cadena= i+","+j	
				if cadena in self.conjuntoPrimeros:
					letra.append(cadena)
					filas.append(letra)
		print(self.terminales)
		
		tabla=tt.Texttable()
		cabecera=self.terminales
		tabla.header(cabecera)
		for i in cabecera:
			print(i)
		
	
		for columna in zip(columnas):
			tabla.add_row(columna)
		s=tabla.draw()
		print(s)
		
				
lexer=ll1("gramatica.txt")
