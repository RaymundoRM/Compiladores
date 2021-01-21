import string
import tkinter.messagebox as ms
import re

class Thompson:
	def convertir(self,cadena):
		cadena=cadena
		automataFinal=[]
		abecedario=string.ascii_lowercase #arroja las letras en minusculas
		error=False
		lenguaje=[]
		separador_or = []
		separador_estrella = []
		separador_positiva = []
		operadores=["+","|","*"]
		lenguaje+=operadores
		for i in abecedario:
			lenguaje.append(i)	#obtenemos el abecedario en minusculas por que es lo que vamos a checar primero en la caden
		#bloque para validar si la cadena ingresada es permitida por el lenguaje
		for i  in cadena:
			if i not in lenguaje:
				error=True
			else:
				error=False
		if(error == True):
			ms.showerror('Cadena Invalida', 'Ingresa otra cadena')
		
		#fin de bloque para validar cadena
		automataFinal.append(self.obtenerCerraduraEstrella(cadena))
		automataFinal.append(self.obtenerCerraduraPositiva(cadena))
		print(automataFinal)


	def obtenerCerraduraEstrella(self,cadena):
		automata=[]
		expresionNormal=[]
		expresionParentesis=[]
		listaCompleta=[]
		expresionNormal=re.findall("\w\*",cadena)
		expresionParentesis=re.findall("\(\w+\)\*",cadena)
		listaCompleta+=expresionNormal
		listaCompleta+=expresionParentesis
		automata.append(self.plantillaEstrella(listaCompleta))
		return automata

	def obtenerCerraduraPositiva(self,cadena):
		automata=[]
		listaCompleta=[]
		expresionNormal=[]
		expresionParentesis=[]
		expresionNormal=re.findall("\w\+",cadena)
		expresionParentesis=re.findall("\(\w+\)\+",cadena)
		listaCompleta+=expresionNormal
		listaCompleta+=expresionParentesis
		automata.append(self.plantillaPositiva(listaCompleta))
		return automata

	def plantillaPositiva(self,Lista):
		automatas=[]
		for i in Lista:
			i=i.replace("+","")
			contador1=1;
			contador2=2;
			if len(i) == 1: 
				lista_nueva=[]
				lista_nueva.append("Estado"+str(contador1)+"->Estado"+str(contador2)+","+i)
				lista_nueva.append("Estado"+str((contador1+1))+"->Estado"+str((contador2+1))+",E")
				lista_nueva.append("Estado"+str((contador1+1))+"->Estado"+str((contador2+3))+",E")
				lista_nueva.append("Estado"+str((contador1+2))+"->Estado"+str(contador2+2)+","+i)
				lista_nueva.append("Estado"+str((contador1+3))+"->Estado"+str(contador2+1)+",E")
				lista_nueva.append("Estado"+str((contador1+3))+"->Estado"+str(contador2+3)+",E")
				automatas.append(lista_nueva)
			if len(i) > 1:
				lista_nueva=[]
				i=i.replace("(","")
				i=i.replace(")","")
				n=1
				contador1=1+len(i)
				contador2=2+len(i)
				for letra in i:
					lista_nueva.append("Estado"+str((n))+"->Estado"+str((n+1))+","+letra)
					n=n+1
				lista_nueva.append("Estado"+str((contador1))+"->Estado"+str(contador2)+",E")
				lista_nueva.append("Estado"+str((contador1))+"->Estado"+str(contador2+1+len(i))+",E")
					
				for letra in i:
					lista_nueva.append("Estado"+str((n+1))+"->Estado"+str((n+2))+","+letra)
					n=n+1
					
				lista_nueva.append("Estado"+str((contador1+len(i)+1))+"->Estado"+str(contador2+len(i)+1)+",E")
				lista_nueva.append("Estado"+str((contador1+len(i)+1))+"->Estado"+str(contador2+len(i)-4)+",E")
				automatas.append(lista_nueva)
			
		return automatas

	def plantillaEstrella(self,Lista):
		automatas=[]
		for i in Lista:
			i=i.replace("*","")
			contador1=1;
			contador2=2;
			if len(i) == 1: 	
				lista_nueva=[]
				lista_nueva.append("Estado"+str(contador1)+"->Estado"+str(contador2)+",E")
				lista_nueva.append("Estado"+str(contador1)+"->Estado"+str(contador2+2)+",E")
				lista_nueva.append("Estado"+str((contador1+1))+"->Estado"+str((contador2+1))+","+i)
				lista_nueva.append("Estado"+str((contador1+2))+"->Estado"+str(contador2)+",E")
				lista_nueva.append("Estado"+str((contador1+2))+"->Estado"+str(contador2+2)+",E")
				automatas.append(lista_nueva)
			if len(i) > 1:
				lista_nueva=[]
				i=i.replace("(","")
				i=i.replace(")","")
				lista_nueva.append("Estado"+str(contador1)+"->Estado"+str(contador2)+",E")
				lista_nueva.append("Estado"+str(contador1)+"->Estado"+str(contador2+1+len(i))+",E")
				n=1
				for letra in i:				
					lista_nueva.append("Estado"+str((contador1+n))+"->Estado"+str((contador2+n))+","+letra)
					n=n+1
				lista_nueva.append("Estado"+str((contador1+1+len(i)))+"->Estado"+str(contador2)+",E")
				lista_nueva.append("Estado"+str((contador1+1+len(i)))+"->Estado"+str(contador2+1+len(i))+",E")
				automatas.append(lista_nueva)
		return automatas
			

automata= Thompson()

automata.convertir("a+b+c*")
