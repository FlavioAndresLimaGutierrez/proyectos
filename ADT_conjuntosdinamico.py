class ConjuntoDinamico:
    """
    ADT Conjunto implementado con estructura dinámica.
    Internamente usa listas, pero se maneja como conjunto.
    """

    def __init__(self, datos_iniciales=None):
        """
        Inicializa el conjunto dinámico con valores opcionales.

        Args:
            datos_iniciales (iterable, optional): Colección inicial de elementos.
        """
        self.__items = []
        if datos_iniciales:
            for dato in datos_iniciales:
                self.agregar(dato)

    # ==================== MÉTODOS GETTER ====================

    def get_elementos(self):
        """Devuelve una copia de los elementos actuales."""
        return list(self.__items)

    def get_tamano(self):
        """Devuelve cuántos elementos contiene el conjunto."""
        return len(self.__items)

    def contiene(self, valor):
        """Indica si un valor está presente en el conjunto."""
        return valor in self.__items

    def esta_vacio(self):
        """Indica si el conjunto está vacío."""
        return self.get_tamano() == 0

    # ==================== MÉTODOS SETTER ====================

    def agregar(self, valor):
        """Agrega un valor si aún no existe en el conjunto."""
        if valor not in self.__items:
            self.__items.append(valor)
            return True
        return False

    def eliminar(self, valor):
        """Elimina un valor si está en el conjunto."""
        if valor in self.__items:
            self.__items.remove(valor)
            return True
        return False

    def limpiar(self):
        """Vacía por completo el conjunto."""
        self.__items.clear()

    # ==================== OPERACIONES DE CONJUNTO ====================

    def union(self, otro):
        """Devuelve la unión con otro conjunto dinámico."""
        resultado = ConjuntoDinamico(self.__items)
        for val in otro.get_elementos():
            resultado.agregar(val)
        return resultado

    def interseccion(self, otro):
        """Devuelve la intersección con otro conjunto dinámico."""
        return ConjuntoDinamico(
            [val for val in self.__items if otro.contiene(val)]
        )

    def diferencia(self, otro):
        """Devuelve la diferencia con otro conjunto dinámico."""
        resultado = ConjuntoDinamico(self.__items)
        for val in otro.get_elementos():
            resultado.eliminar(val)
        return resultado

    def es_subconjunto(self, otro):
        """Indica si este conjunto es subconjunto del otro."""
        return all(otro.contiene(val) for val in self.__items)

    # ==================== MÉTODOS ESPECIALES ====================

    def __str__(self):
        return f"Conjunto({self.__items})"

    def __len__(self):
        return self.get_tamano()

    def __contains__(self, valor):
        return self.contiene(valor)


def demo():
    """Pequeña demostración del funcionamiento del conjunto dinámico."""
    print("===== DEMO CONJUNTO DINÁMICO =====")
    a = ConjuntoDinamico([1, 2, 3, 4])
    b = ConjuntoDinamico([3, 4, 5])

    print("Conjunto A:", a)
    print("Conjunto B:", b)

    print("Unión:", a.union(b))
    print("Intersección:", a.interseccion(b))
    print("Diferencia A-B:", a.diferencia(b))
    print("¿A es subconjunto de B?", a.es_subconjunto(b))
    print("Tamaño de A:", len(a))
    print("¿2 en A?", 2 in a)
    print("¿10 en A?", 10 in a)


if __name__ == "__main__":
    demo()

