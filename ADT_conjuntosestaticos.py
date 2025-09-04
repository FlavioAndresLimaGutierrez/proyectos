"""
ADT Conjunto implementado con Estructura Estática
(Usa listas y funciones puras - sin objetos ni clases)
"""

# ==================== OPERACIONES BÁSICAS ====================

def crear_conjunto(elementos=None):
    """
    Crea un nuevo conjunto estático sin duplicados.
    """
    if elementos is None:
        return []
    
    conjunto = []
    for elemento in elementos:
        if elemento not in conjunto:
            conjunto.append(elemento)
    return conjunto


def agregar_elemento(conjunto, elemento):
    """
    Retorna un nuevo conjunto con el elemento agregado si no existe.
    """
    if elemento not in conjunto:
        return conjunto + [elemento]
    return conjunto.copy()


def eliminar_elemento(conjunto, elemento):
    """
    Retorna un nuevo conjunto sin el elemento indicado.
    """
    if elemento in conjunto:
        nuevo_conjunto = conjunto.copy()
        nuevo_conjunto.remove(elemento)
        return nuevo_conjunto
    return conjunto.copy()


def contiene_elemento(conjunto, elemento):
    """Verifica si el conjunto contiene un elemento."""
    return elemento in conjunto


def obtener_tamano(conjunto):
    """Retorna el número de elementos del conjunto."""
    return len(conjunto)


def esta_vacio(conjunto):
    """Retorna True si el conjunto está vacío."""
    return len(conjunto) == 0


# ==================== OPERACIONES DE CONJUNTO ====================

def union(conjunto_a, conjunto_b):
    """Retorna la unión de dos conjuntos."""
    resultado = conjunto_a.copy()
    for elemento in conjunto_b:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def interseccion(conjunto_a, conjunto_b):
    """Retorna la intersección de dos conjuntos."""
    return [e for e in conjunto_a if e in conjunto_b]


def diferencia(conjunto_a, conjunto_b):
    """Retorna la diferencia A - B."""
    return [e for e in conjunto_a if e not in conjunto_b]


def es_subconjunto(conjunto_a, conjunto_b):
    """Verifica si A es subconjunto de B."""
    return all(e in conjunto_b for e in conjunto_a)


# ==================== FUNCIÓN DE DEMOSTRACIÓN ====================

def demostrar_conjunto_estatico():
    print("=== ADT CONJUNTO - ESTRUCTURA ESTÁTICA ===\n")
    
    # Crear conjuntos iniciales
    print("1. CREACIÓN DE CONJUNTOS:")
    conjunto_a = crear_conjunto([1, 2, 3, 4])
    conjunto_b = crear_conjunto([3, 4, 5, 6])
    print(f"Conjunto A → {conjunto_a}")
    print(f"Conjunto B → {conjunto_b}")
    
    # Operaciones básicas
    print("\n2. OPERACIONES BÁSICAS:")
    print(f"Tamaño de A: {obtener_tamano(conjunto_a)}")
    print(f"¿A contiene 3? {'Sí' if contiene_elemento(conjunto_a, 3) else 'No'}")
    print(f"¿A está vacío? {'Sí' if esta_vacio(conjunto_a) else 'No'}")
    
    # Modificar conjuntos
    print("\n3. MODIFICACIÓN DE CONJUNTOS:")
    conjunto_a = agregar_elemento(conjunto_a, 5)
    print(f"A después de agregar 5 → {conjunto_a}")
    conjunto_a = eliminar_elemento(conjunto_a, 2)
    print(f"A después de eliminar 2 → {conjunto_a}")
    
    # Operaciones de conjunto
    print("\n4. OPERACIONES ENTRE CONJUNTOS:")
    print(f"A ∪ B → {union(conjunto_a, conjunto_b)}")
    print(f"A ∩ B → {interseccion(conjunto_a, conjunto_b)}")
    print(f"A - B → {diferencia(conjunto_a, conjunto_b)}")
    print(f"¿A es subconjunto de B? {'Sí' if es_subconjunto(conjunto_a, conjunto_b) else 'No'}")
    
    # Conjunto vacío
    print("\n5. CONJUNTO VACÍO:")
    conjunto_vacio = crear_conjunto()
    print(f"Conjunto vacío → {conjunto_vacio}")
    print(f"¿Está vacío? {'Sí' if esta_vacio(conjunto_vacio) else 'No'}")


if __name__ == "__main__":
    demostrar_conjunto_estatico()
    print("\n=== DEMOSTRACIÓN FINALIZADA ===")

