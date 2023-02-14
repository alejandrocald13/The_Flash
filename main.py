print('Mi nombre es Roberto Alejandro Calderón Martínez')
print('Mi carné estudiantil es: 1557723')
print('Resido en Quetzaltenango.')
print('Mi universidad es la Universidad Rafael Landivar, Campus de Quetzaltenango.')

import os

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()
