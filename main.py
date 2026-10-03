from catalogo import Catalogo

catalogo = Catalogo()

print('=== DINALPARTES S.A.S. ===')
print('Sistema de Navegación de Catálogo')
print('1. Buscar por referencia')
print('2. Buscar por marca')
print('3. Buscar por vehículo')

opcion = input('Seleccione una opción: ')

if opcion == '1':
    criterio = input('Ingrese la referencia: ')
    resultados = catalogo.buscar_por_referencia(criterio)
elif opcion == '2':
    criterio = input('Ingrese la marca: ')
    resultados = catalogo.buscar_por_marca(criterio)
elif opcion == '3':
    criterio = input('Ingrese el vehículo: ')
    resultados = catalogo.buscar_por_vehiculo(criterio)
else:
    resultados = []

print('\nResultados encontrados:')
for p in resultados:
    print('-', p['nombre'])

if not resultados:
    print('No se encontraron productos.')
