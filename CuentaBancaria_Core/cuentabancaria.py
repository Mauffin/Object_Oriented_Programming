
class CuentaBancaria:
    nombre_banco = "banco dojo"
    cuentas = [] # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interés, balance):
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("saldo insuficiente")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"{self.balance}")
        
    def generar_interés(self):
        if self.balance > 0:
            self.balance -=(self.balance * self.tasa_interés)
        return self

    @classmethod
    def mostrar_balance_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
