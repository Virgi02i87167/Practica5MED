def ingresardatos():
    n = int(input("Ingrese una cantidad de datos: "))
    datos = []
    for i in range(n):
        dato = float(input(f"Ingrese un dato {i + 1}: "))
        datos.append(dato)
    return datos

def ordenarlista(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n-i-1):
            if datos[j] > datos[j+1]:
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos

def sumatoria(datos):
    suma = 0
    for dato in datos:
        suma += dato
    return suma

def calcularmedia(datos):
    suma = sumatoria(datos)
    n = len(datos)
    if n == 0:
        return None  
    media = suma / n
    return media


def mediana(datos):
    datosordenados = ordenarlista(datos)
    n = len(datosordenados)
    if n % 2 == 1:
        mediana = datosordenados[n // 2]
    else:
        mediana = (datosordenados[n // 2 - 1] + datosordenados[n // 2]) / 2
    return mediana


def moda(datos):
    frecuencias = {}
    for dato in datos:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1
    
    moda = []
    maxfrecuencia = max(frecuencias.values())
    
    for dato, frecuencia in frecuencias.items():
        if frecuencia == maxfrecuencia:
            moda.append(dato)
    
    return moda

def desviacionestandar(datos):
    media = calcularmedia(datos)
    n = len(datos)
    if n == 0:
        return None  
    
    suma_cuadrados_diferencia = 0
    for dato in datos:
        suma_cuadrados_diferencia += (dato - media) ** 2
    
    desviacion_estandar = (suma_cuadrados_diferencia / n) ** 0.5
    return desviacion_estandar

datos = ingresardatos()
print("Datos ingresados:", datos)
print("Datos ordenados:", ordenarlista(datos))
print("Sumatoria:", sumatoria(datos))
print("Media:", calcularmedia(datos))
print("Mediana:", mediana(datos))
print("Moda:", moda(datos))
print("Desviación estándar:", desviacionestandar(datos))