
# ----------------------------------------------------------------------------------------------------------------------------
def validar_numero (numero:int,mensaje_error:str,minimo:int,maximo:int)->int:
        
        """Esta función solicita al usuario ingresar un número entero y lo valida para asegurarse de que esté dentro del rango especificado y 
        sea un número entero válido. Si la entrada no es un número entero o está fuera del rango especificado, se solicita al usuario que ingrese nuevamente 
        el número hasta que se proporcione una entrada válida.
        Args:
            numero (int): El número entero a validar.
            mensaje_error (str): El mensaje de error a mostrar si la validación falla o la entrada no es válida.
            minimo (int): El valor mínimo permitido para el número.
            maximo (int): El valor máximo permitido para el número.
        Returns:
            int: El número entero validado"""
        while numero % 1 != 0 or (numero > maximo or numero < minimo):
            numero = input(mensaje_error)
            numero = float(numero)

        return int(numero)
       
# ----------------------------------------------------------------------------------------------------------------------------




        

        

  