Nombre = input("Ingrese su nombre: ")
Dias = 7
Salario = 785000
Prima = (Salario * Dias)/360
Cesantias = (Salario * Dias)/360
Intereses_cesantias = (Cesantias * 0.12)/Dias
Vacaciones = Salario * Dias / 720
Liquidacion = (Prima+Cesantias+Intereses_cesantias+Vacaciones)



print(f"Señor {Nombre}"
      f" por los {Dias} dias laborados y salario ${Salario},"
      f"su liquidacion se compone asi: ")
print(f"prima: {Prima}")
print(f"cesabtias: {Cesantias}")
print(f"intereses cesantias: {Intereses_cesantias}")
print(f"vacaciones: {Vacaciones}")
print(f"liquidacuion: {Liquidacion}")
