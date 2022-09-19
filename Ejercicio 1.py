# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:03:49 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


# Esta función eliminará los valores duplicados de una lista y retornará una lista nueva sin los valores duplicados.
def eliminar_duplicados(lista):
    lista_nueva = []  # Se inicializa una nueva lista vacía
    for i in lista:  # Para cada elemento en 'lista'
        # Si el elemento de la lista no se encuentra en la lista nueva (vacía)
        if i not in lista_nueva:
            lista_nueva.append(i)  # Se agrega a nuestra nueva lista
    return lista_nueva  # Retornamos la lista nueva sin valores duplicados


# Programa principal
n = int(input("¿Cuántos números desea ingresar?: "))

lista = []  # Se inicializa la lista vacía para luego preguntar al usuario por cada valor que desee ingresar
for n_actuales in range(n):
    num = int(input(f"Ingrese el número {n_actuales+1} de la lista: "))
    lista.append(num)  # Se agrega el valor ingresado a la lista

# Se llama a la función para eliminar los duplicados y su resultado se guarda en 'duplicados'
duplicados = eliminar_duplicados(lista)

print(f"La lista original es: {lista}")
print(f"La lista sin valores duplicados es: {duplicados}")  # Resultado final
