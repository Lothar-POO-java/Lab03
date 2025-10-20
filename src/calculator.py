class Calculator: # Lothar
    # Suma dos números
    def sumar(self, a, b): # 2 usages (2 dynamic) & Lothar
        return a + b

    # Resta dos números
    def restar(self, a, b): # 2 usages (2 dynamic) & Lothar
        return a - b

    # Divide dos número
    def dividir(self, a, b): # 3 usages (3 dynamic) & Lothar
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    # Multiplica dos número
    def multiplicar(self, a, b): # 2 usages (2 dynamic) & Lothar
        return a * b

    # Calcula la potencia
    def potencia(self, base, exponente): # 2 usages (2 dynamic) & Lothar
        if exponente < 0:
            return 1 / (base ** abs(exponente))
        return base ** exponente