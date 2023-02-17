'''

TALLER: CICLO MIENTRAS Y SELECTOR MÚLTIPLE

El Fondo de empleados del ITM ha decidido subsidiar una póliza de salud a sus asociados. El valor de la póliza es
el equivalente al 5% del Salario Básico del asociado. El valor subsidiado por el Fondo dependerá del estrato del
asociado así:
Estrato:
1. 50%
2. 40%
3. 30%
4. 20%
Otro. 10%
El programa debe mostrar a cada asociado:
a. El valor de la póliza
b. El valor que debe cubrir el asociado
c. El valor subsidiado por el Fondo
El programa debe mostrar un resumen al final indicando:
a. Cuantos subsidios se entregaron por cada estrato
d. El monto total por subsidios que debe desembolsar el Fondo
e. El promedio subsidiado por asociado (promedio general)


Datos de prueba

Asociado    Estrato     Salario     Valor Póliza    Valor Subsidio      Valor asociado

1               1     $ 1.200.000     $ 60.000          $ 30.000            $ 30.000
2               2     $ 1.500.000     $ 75.000          $ 30.000            $ 45.000
3               1     $ 1.300.000     $ 65.000          $ 32.500            $ 32.500
4               4     $ 2.800.000     $ 140.000         $ 28.000            $ 112.000
5               3     $ 2.100.000     $ 105.000         $ 31.500            $ 73.500
6               5     $ 3.200.000     $ 160.000         $ 16.000            $ 144.000
7               6     $ 3.800.000     $ 190.000         $ 19.000            $ 171.000
8               2     $ 2.000.000     $ 100.000         $ 40.000            $ 60.000

RESUMEN (Si el programa está bien deberá mostrar estor resultados al final)
Subsidios entregados por estrato:

1. 2
2. 2
3. 1
4. 1
Otro. 2

Total a desembolsar por subsidio: $227.000
Promedio subsidiado por asociado: $28.375

'''
datos_suministrados = open ("Datos_Base.txt","w")
datos_suministrados.write("Estrato\tSalario\n")
datos_suministrados.write("1\t1200000\n")

datos_suministrados= open ("Datos_Base.txt", "r")
for line in datos_suministrados:
    line= line.strip()
    print(line)