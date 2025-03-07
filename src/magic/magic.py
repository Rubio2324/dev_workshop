class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
    
        fib = [0, 1]  
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])  
        return fib[n]
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        fib = [0, 1]  
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])  
        return fib
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
        i += 6

        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        if n < 2:
            return []

        es_primo = [True] * (n + 1)  
        es_primo[0] = es_primo[1] = False  

        for i in range(2, int(n**0.5) + 1):  
            if es_primo[i]: 
                for j in range(i * i, n + 1, i):
                    es_primo[j] = False

        return [x for x in range(n + 1) if es_primo[x]]
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False

        suma_divisores = 1  
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma_divisores += i
            if i != n // i:  
                suma_divisores += n // i
    
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas <= 0:
            return []

        triangulo = [[1]]  

        for i in range(1, filas):
            fila_anterior = triangulo[-1]  
        nueva_fila = [1]  

        
        for j in range(1, len(fila_anterior)):
            nueva_fila.append(fila_anterior[j - 1] + fila_anterior[j])

        nueva_fila.append(1) 
        triangulo.append(nueva_fila)

        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        def mcd(x, y):
            while y:
                x, y = y, x % y
        return abs(x)

        return abs(a * b) // mcd(a, b) if a and b else 0
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        num_str = str(n)  
        num_digitos = len(num_str)  
        suma = sum(int(d) ** num_digitos for d in num_str)  
        return suma == n 
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        return sum(int(d) for d in str(abs(n)))