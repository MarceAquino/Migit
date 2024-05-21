cadena = "                  hola mundo   "
cadena = cadena.strip() #quita todos los espacios de la lista se tiene q guardar ya que la cadena no es mutable 
print(cadena)

cadena = "####hola mundo####"
cadena = cadena.strip("#") # borra lo q le pongas adelante o atras  lstrip rstrip inzquierda o derecha mismo metodo 
print(cadena)


cadena = "hola mundo"
cadena = cadena.upper() # trasforma todo en mayusculas 
print(cadena)


cadena = "hola mundo"
cadena = cadena.lower() # trasforma todo en minuscula
print(cadena)


cadena = "hola mundo"
cadena = cadena.capitalize() #pasa la primer letra en mayuscula y el resto en minuscula 
print(cadena)

cadena = "hola mundo hola hola "
cadena = cadena.replace("hola","") # recibe un parametro y se le indica que modificar 
print(cadena)

cadena = "Python,Java,C" #El método split divide una cadena en subcadenas y las devuelve almacenadas en una lista
print(cadena.split(",")) 
#['Python', 'Java', 'C']

cadena = "+"
cadena = cadena.join(["A", "B", "C"]) #El método join devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parámetro.
print(cadena) # A+B+C


#El método zfill rellena la cadena con ceros a la izquierda hasta llegar a la longitud pasada como parámetro.
cadena = "314"
print(cadena.zfill(6))
#000314


#El método isalpha devuelve True si todos los caracteres son alfabéticos, False de lo contrario.
cadena = "Hola Mundo"
print(cadena.isalpha()) 
# False -> por el espacio

cadena = "HolaMundo"
print(cadena.isalpha()) 
# True

#El método isalnum devuelve True si todos los caracteres son alfanumericos.
cadena = "HolaMundo"
print(cadena.isalnum()) 
# False -> por el espacio

cadena = "Hola99Mundo"
print(cadena.isalnum()) 
# True

#El método isdigit devuelve True si todos los caracteres son numericos.
cadena = "Hola Mundo"
print(cadena.isdigit()) 
# False -> por el espacio

cadena = "1122222"
print(cadena.isdigit()) 
# True

#El método count permite contar las veces que otra cadena se encuentra dentro de la primera. 
cadena = "Hola Mundo Hola"
print(cadena.count("la")) # 2

#En el método format las llaves, llamadas campos de formato, son reemplazadas con los valores de las variables pasadas.

nombre_usuario="JUAN"
edad_usuario=35
cadena = "Nombre: {1}, Edad: {0}"
print(cadena.format(edad_usuario,
nombre_usuario))
#Nombre: JUAN, Edad: 35






hola = "Trueno | Sesión #1"

cadena = hola.split("|")

colaborador = cadena[0]

sesion = cadena[1]
sesion = sesion.replace("Sesión #", "")

print(colaborador)
print(sesion)