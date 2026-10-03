from productos import PRODUCTOS

class Catalogo:
    def buscar_por_referencia(self, referencia):
        return [p for p in PRODUCTOS if referencia.lower() in p['referencia'].lower()]

    def buscar_por_marca(self, marca):
        return [p for p in PRODUCTOS if marca.lower() in p['marca'].lower()]

    def buscar_por_vehiculo(self, vehiculo):
        return [p for p in PRODUCTOS if vehiculo.lower() in p['vehiculo'].lower()]
