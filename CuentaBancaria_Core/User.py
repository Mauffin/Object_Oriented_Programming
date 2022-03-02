from cuentabancaria import CuentaBancaria
class User:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = {"Principal": CuentaBancaria(5,100),
                        "ahorros": CuentaBancaria(0,100000)
                        }

    def balance_usuario(self):
        print(f"cuenta:{self.nombre},Cuenta principal {self.cuenta['Principal'].mostrar_info_cuenta()}")
        print(f"cuenta: {self.nombre},Cuenta de ahorros {self.cuenta['ahorros'].mostrar_info_cuenta()}")
        return self


    # def deposito(self):
    #     self.cuenta.deposito(100)
    #     print(self.cuenta.balance)

damian = User("damian")


damian.cuenta['Principal']
damian.balance_usuario()