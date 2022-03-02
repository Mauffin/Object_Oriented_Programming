from cuentabancaria import CuentaBancaria

damian = CuentaBancaria (0.05,1000)
cardenas = CuentaBancaria(0.05,1000)


damian.depósito(100).depósito(100).depósito(100).retiro(300).generar_interés().mostrar_info_cuenta()
cardenas.depósito(200).depósito(200).retiro(150).retiro(100).retiro(100).generar_interés().mostrar_info_cuenta()

# CuentaBancaria.mostrar_balance_cuentas()
