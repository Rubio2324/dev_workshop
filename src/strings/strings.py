class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())

        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        cadena_invertida = ""
        for caracter in texto:
            cadena_invertida = caracter + cadena_invertida  
        return cadena_invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
                
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter.isalpha() and caracter not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        return " ".join(texto.split())
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if not texto:
            return False

        if texto[0] in ('-', '+'):
            texto = texto[1:] 

        return all('0' <= char <= '9' for char in texto) and len(texto) > 0
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""

        for caracter in texto:
            if 'A' <= caracter <= 'Z': 
                nueva_letra = chr(((ord(caracter) - ord('A') + desplazamiento) % 26) + ord('A'))
            elif 'a' <= caracter <= 'z':  
                nueva_letra = chr(((ord(caracter) - ord('a') + desplazamiento) % 26) + ord('a'))
        else:
            nueva_letra = caracter 

        resultado += nueva_letra

        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        for caracter in texto:
            if 'A' <= caracter <= 'Z':  # Letras mayúsculas
                nueva_letra = chr(((ord(caracter) - ord('A') - desplazamiento) % 26) + ord('A'))
            elif 'a' <= caracter <= 'z':  # Letras minúsculas
                nueva_letra = chr(((ord(caracter) - ord('a') - desplazamiento) % 26) + ord('a'))
        else:
            nueva_letra = caracter  # No modifica otros caracteres

        resultado += nueva_letra

        return resultado
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posiciones = []
        longitud_texto = len(texto)
        longitud_subcadena = len(subcadena)

        for i in range(longitud_texto - longitud_subcadena + 1):
            if texto[i:i + longitud_subcadena] == subcadena:
                posiciones.append(i)

        return posiciones
    