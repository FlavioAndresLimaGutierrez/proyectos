"""
ADT Conjunto con Almacenamiento en Disco
Los datos se guardan en archivos JSON de forma persistente.
"""

import json
import os

# ==================== OPERACIONES BÁSICAS ====================

def crear_conjunto_disco(ruta_archivo, valores=None):
    """
    Crea un archivo JSON que representa un conjunto en disco.
    
    Args:
        ruta_archivo (str): Ruta o nombre del archivo.
        valores (list, optional): Elementos iniciales.
    
    Returns:
        bool: True si se creó sin errores.
    """
    try:
        datos = valores or []
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f)
        return True
    except Exception as e:
        print(f"[Error] Creando conjunto: {e}")
        return False

def cargar_conjunto_disco(ruta_archivo):
    """Devuelve la lista de elementos desde el archivo JSON."""
    try:
        if not os.path.exists(ruta_archivo):
            return []
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Error] Cargando conjunto: {e}")
        return []

def guardar_conjunto_disco(ruta_archivo, elementos):
    """Guarda la lista de elementos en un archivo JSON."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(elementos, f)
        return True
    except Exception as e:
        print(f"[Error] Guardando conjunto: {e}")
        return False

# ==================== OPERACIONES DEL CONJUNTO ====================

def agregar_elemento_disco(ruta_archivo, valor):
    """Agrega un elemento si no está presente."""
    elementos = cargar_conjunto_disco(ruta_archivo)
    if valor not in elementos:
        elementos.append(valor)
        return guardar_conjunto_disco(ruta_archivo, elementos)
    return False

def eliminar_elemento_disco(ruta_archivo, valor):
    """Elimina un elemento si existe en el conjunto en disco."""
    elementos = cargar_conjunto_disco(ruta_archivo)
    if valor in elementos:
        elementos.remove(valor)
        return guardar_conjunto_disco(ruta_archivo, elementos)
    return False

def contiene_elemento_disco(ruta_archivo, valor):
    """Indica si un valor está en el conjunto guardado en disco."""
    return valor in cargar_conjunto_disco(ruta_archivo)

def obtener_tamano_disco(ruta_archivo):
    """Devuelve el número de elementos en el archivo JSON."""
    return len(cargar_conjunto_disco(ruta_archivo))

def esta_vacio_disco(ruta_archivo):
    """Indica si el archivo JSON representa un conjunto vacío."""
    return obtener_tamano_disco(ruta_archivo) == 0

# ==================== OPERACIONES AVANZADAS ====================

def union_disco(archivo_a, archivo_b, archivo_destino):
    """Crea la unión de dos conjuntos en disco y la guarda en otro archivo."""
    conjunto_a = cargar_conjunto_disco(archivo_a)
    conjunto_b = cargar_conjunto_disco(archivo_b)

    resultado = list(conjunto_a)  # copia inicial
    for val in conjunto_b:
        if val not in resultado:
            resultado.append(val)
    return guardar_conjunto_disco(archivo_destino, resultado)

def limpiar_conjunto_disco(ruta_archivo):
    """Vacía el archivo JSON, dejando el conjunto sin elementos."""
    return guardar_conjunto_disco(ruta_archivo, [])

# ==================== DEMOSTRACIÓN ====================

def demo_conjunto_disco():
    """Ejemplo práctico del uso del ADT Conjunto en disco."""
    print("=== DEMO ADT CONJUNTO - DISCO ===")

    archivo_a = "A.json"
    archivo_b = "B.json"
    archivo_union = "Union.json"

    # Crear conjuntos iniciales
    crear_conjunto_disco(archivo_a, [1, 2, 3])
    crear_conjunto_disco(archivo_b, [3, 4, 5])

    print(f"A inicial: {cargar_conjunto_disco(archivo_a)}")
    print(f"B inicial: {cargar_conjunto_disco(archivo_b)}")

    # Operaciones básicas
    agregar_elemento_disco(archivo_a, 10)
    eliminar_elemento_disco(archivo_a, 2)

    print(f"A modificado: {cargar_conjunto_disco(archivo_a)}")
    print(f"Tamaño de A: {obtener_tamano_disco(archivo_a)}")
    print(f"¿Contiene 3? {contiene_elemento_disco(archivo_a, 3)}")

    # Unión
    union_disco(archivo_a, archivo_b, archivo_union)
    print(f"A ∪ B: {cargar_conjunto_disco(archivo_union)}")

    # Limpieza
    limpiar_conjunto_disco(archivo_a)
    print(f"A después de limpiar: {cargar_conjunto_disco(archivo_a)}")
    print("¿A está vacío?", esta_vacio_disco(archivo_a))

if __name__ == "__main__":
    demo_conjunto_disco()
    print("\n=== DEMO COMPLETADA ===")

