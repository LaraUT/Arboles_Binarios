class NodoArbol:
    def __init__(self, dato):
        # Constructor para inicializar un nodo con un dato dado.
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        # Constructor para inicializar un árbol binario vacío sin raíz.
        self.raiz = None

    def agregar(self, dato):
        # Agrega un nuevo nodo con el dato dado al árbol.
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._agregar_recursivo(self.raiz, dato)

    def _agregar_recursivo(self, nodo, nuevo_dato):
        # Método privado recursivo para agregar un nodo al árbol.
        if nuevo_dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nuevo_dato)
            else:
                self._agregar_recursivo(nodo.izquierda, nuevo_dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nuevo_dato)
            else:
                self._agregar_recursivo(nodo.derecha, nuevo_dato)

    def mostrar(self):
        # Muestra todo el árbol utilizando un método recursivo auxiliar.
        self._mostrar_recursivo(self.raiz, 0)

    def _mostrar_recursivo(self, nodo, nivel):
        # Método privado recursivo para mostrar el árbol de forma rotada.
        if nodo is not None:
            self._mostrar_recursivo(nodo.derecha, nivel + 1)
            print("  00000     " * nivel + str(nodo.dato))
            self._mostrar_recursivo(nodo.izquierda, nivel + 1)

    def buscar(self, dato):
        # Inicia la búsqueda de un dato específico en el árbol.
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        # Método privado recursivo para buscar un dato en el árbol.
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierda, dato)
        return self._buscar_recursivo(nodo.derecha, dato)

    def eliminar(self, dato):
        # Inicia la eliminación de un nodo con el dato especificado.
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo, dato):
        # Método privado recursivo para eliminar un nodo con el dato dado.
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo

    def _encontrar_minimo(self, nodo):
        # Encuentra el valor mínimo en un subárbol dado.
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.dato

    def recorrer_preorden(self):
        # Realiza un recorrido en preorden y devuelve una lista de nodos visitados.
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        # Método auxiliar para recorrido en preorden.
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorden(nodo.izquierda, resultado)
            self._preorden(nodo.derecha, resultado)

    def recorrer_inorden(self):
        # Realiza un recorrido en inorden y devuelve una lista de nodos visitados.
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        # Método auxiliar para recorrido en inorden.
        if nodo is not None:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self._inorden(nodo.derecha, resultado)

    def recorrer_postorden(self):
        # Realiza un recorrido en postorden y devuelve una lista de nodos visitados.
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        # Método auxiliar para recorrido en postorden.
        if nodo is not None:
            self._postorden(nodo.izquierda, resultado)
            self._postorden(nodo.derecha, resultado)
            resultado.append(nodo.dato)

# Llamada a la ejecución de la clase
arbol = ArbolBinario()

def menu():
    opcion = 0
    while opcion != 8:
        print("1.- AGREGAR UN ELEMENTO AL ÁRBOL")
        print("2.- BUSCAR UN ELEMENTO EN EL ÁRBOL")
        print("3.- ELIMINAR UN ELEMENTO DEL ÁRBOL")
        print("4.- MOSTRAR EL ÁRBOL COMPLETO")
        print("5.- RECORRER EL ÁRBOL EN PREORDEN")
        print("6.- RECORRER EL ÁRBOL EN INORDEN")
        print("7.- RECORRER EL ÁRBOL EN POSTORDEN")
        print("8.- SALIR")

        opcion = int(input("ELIGE UNA OPCIÓN: "))
        print("\n" * 2)

        if opcion == 1:
            # AGREGAR ELEMENTOS
            elemento_para_agregar = int(input("INGRESA EL ELEMENTO: "))
            arbol.agregar(elemento_para_agregar)
            print("\n")

        elif opcion == 2:
            # BUSCAR ELEMENTOS
            dato_buscar = int(input("¿QUÉ NÚMERO QUIERES BUSCAR? "))
            nodo_encontrado = arbol.buscar(dato_buscar)
            if nodo_encontrado:
                print(f"EL ELEMENTO {dato_buscar} EXISTE EN EL ÁRBOL.")
            else:
                print(f"EL ELEMENTO {dato_buscar} NO EXISTE EN EL ÁRBOL\n")

        elif opcion == 3:
            # ELIMINAR ELEMENTOS
            dato_eliminar = int(input("¿QUÉ NÚMERO QUIERES BORRAR? "))
            arbol.eliminar(dato_eliminar)
            print(f"SE ELIMINÓ EL ELEMENTO {dato_eliminar} CORRECTAMENTE DEL ÁRBOL\n")

        elif opcion == 4:
            # MOSTRAR EL ÁRBOL COMPLETO
            arbol.mostrar()
            print("\n")

        elif opcion == 5:
            # RECORRIDO EN PREORDEN
            print("RECORRIDO EN PREORDEN ES: ", arbol.recorrer_preorden())
            print("\n")

        elif opcion == 6:
            # RECORRIDO EN INORDEN
            print("RECORRIDO EN INORDEN ES: ", arbol.recorrer_inorden())
            print("\n")

        elif opcion == 7:
            # RECORRIDO EN POSTORDEN
            print("RECORRIDO EN POSTORDEN ES: ", arbol.recorrer_postorden())
            print("\n")

        elif opcion == 8:
            # SALIR
            print("ADIOS, ¡VUELVE PRONTO! :)\n")

menu()
