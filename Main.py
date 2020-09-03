import json
import webbrowser
import platform
import os
import time
import re
print("Bienvenido a SimpleQl")
comando = ""
BD = []

def cargar(comando):
    mensaje = 0
    Archivos = comando[7:len(comando)].split(", ")
    for x in range(0,len(Archivos)):
        try:
            CargarJson(Archivos[x])
        except:
            print("El archivo "+Archivos[x]+" no se puede encontrar")
            mensaje = 1
    if mensaje == 0:
        print("Archivo(s) cargado(s) con éxito")

def CargarJson(ArchivoActual):
    with open(ArchivoActual) as Contenido:
        Registros = json.load(Contenido)
        for registro in Registros:
            BD.append([registro.get("nombre"),registro.get("edad"),registro.get("activo"),registro.get("promedio")])

def ImprimirTodo():
    for i in range(len(BD)):
        for j in range(4):
            print("[ ",BD[i][j]," ]",end="")
        print()

def ImprimirDonde(comando):
    RegistrosEncontrados = 0
    existe = 0
    nombre = 0
    edad = 0
    activo = 0
    promedio = 0
    todo = 0
    comando = comando.lower().split(" donde ")
    comando1 = comando[0].split(", ")
    condicion = comando[1]
    pattern = re.compile("= |=")
    condicion = condicion.replace('"', "")
    condicion = pattern.split(condicion)
    condicion[0] = condicion[0].replace(" ", "")
    for i in range (len(comando1)):
        if (comando1[i] == "nombre") or (comando1[i] == "edad") or (comando1[i] == "activo") or (comando1[i] == "promedio") or (comando1[i] == "*"):
            existe = 0
            if comando1[i] == "nombre":
                nombre += 1
            if comando1[i] == "edad":
                edad += 1
            if comando1[i] == "activo":
                activo += 1
            if comando1[i] == "promedio":
                promedio += 1
            if comando1[i] == "*":
                todo += 1
        else:
            existe = 1
    if existe == 0 and nombre <= 1 and edad <= 1 and activo <= 1 and promedio <= 1 and todo <= 1:
        for i in range(len(BD)):
            if condicion[0] == "nombre" and str(condicion[1].lower()) == str(BD[i][0].lower()) and todo == 0:
                if nombre == 1:
                    print("[ ", BD[i][0], " ]", end="")
                if edad == 1:
                    print("[ ", BD[i][1], " ]", end="")
                if activo == 1:
                    print("[ ", BD[i][2], " ]", end="")
                if promedio == 1:
                    print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if condicion[0] == "edad" and int(condicion[1]) == int(BD[i][1]) and todo == 0:
                if nombre == 1:
                    print("[ ", BD[i][0], " ]", end="")
                if edad == 1:
                    print("[ ", BD[i][1], " ]", end="")
                if activo == 1:
                    print("[ ", BD[i][2], " ]", end="")
                if promedio == 1:
                    print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if condicion[0] == "activo" and str(condicion[1]).lower() == str(BD[i][2]).lower() and todo == 0:
                if nombre == 1:
                    print("[ ", BD[i][0], " ]", end="")
                if edad == 1:
                    print("[ ", BD[i][1], " ]", end="")
                if activo == 1:
                    print("[ ", BD[i][2], " ]", end="")
                if promedio == 1:
                    print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if condicion[0] == "promedio" and float(condicion[1]) == float(BD[i][3]) and todo == 0:
                if nombre == 1:
                    print("[ ", BD[i][0], " ]", end="")
                if edad == 1:
                    print("[ ", BD[i][1], " ]", end="")
                if activo == 1:
                    print("[ ", BD[i][2], " ]", end="")
                if promedio == 1:
                    print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if todo == 1 and condicion[0] == "nombre" and str(condicion[1].lower()) == str(BD[i][0].lower()):
                print("[ ", BD[i][0], " ]", end="")
                print("[ ", BD[i][1], " ]", end="")
                print("[ ", BD[i][2], " ]", end="")
                print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if todo == 1 and condicion[0] == "edad" and int(condicion[1]) == int(BD[i][1]):
                print("[ ", BD[i][0], " ]", end="")
                print("[ ", BD[i][1], " ]", end="")
                print("[ ", BD[i][2], " ]", end="")
                print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if todo == 1 and condicion[0] == "activo" and str(condicion[1]).lower() == str(BD[i][2]).lower():
                print("[ ", BD[i][0], " ]", end="")
                print("[ ", BD[i][1], " ]", end="")
                print("[ ", BD[i][2], " ]", end="")
                print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados + 1
                print()
            if todo == 1 and condicion[0] == "promedio" and float(condicion[1]) == float(BD[i][3]):
                print("[ ", BD[i][0], " ]", end="")
                print("[ ", BD[i][1], " ]", end="")
                print("[ ", BD[i][2], " ]", end="")
                print("[ ", BD[i][3], " ]", end="")
                RegistrosEncontrados = RegistrosEncontrados +1
                print()
        if RegistrosEncontrados == 0:
            print("No se encontraron coincidencias")
    else:
        print("Estructura del comando invalida, parametros duplicados o un parametro no existe")

def Seleccionar(comando):
    if len(BD) == 0:
        print("El sistema aún no tiene registros")
    else:
        comando = comando[12:len(comando)]
        if comando[0:1] == "*" and len(comando) == 1:
            ImprimirTodo()
        elif re.search(r"donde", comando.lower()).group() == "donde":
            ImprimirDonde(comando)

def Maximo(comando):
    edad = 0
    promedio = 0.01
    comando = comando.split(" ")
    if comando[1].lower() == "edad":
        for i in range(len(BD)):
            if int(BD[i][1]) > edad:
                edad = BD[i][1]
        print("El valor máximo dentro de las edades es: "+str(edad))
    elif comando[1].lower() == "promedio":
        for i in range(len(BD)):
            if float(BD[i][3]) > promedio:
                promedio = BD[i][3]
        print("El valor máximo dentro de los promedios es: " + str(promedio))
    else:
        print("Comando de maximizar no valido")

def Minimo(comando):
    edad = 99999999999999
    promedio = 9999999999999.9999
    comando = comando.split(" ")
    if comando[1].lower() == "edad":
        for i in range(len(BD)):
            if int(BD[i][1]) < edad:
                edad = BD[i][1]
        print("El valor mínimo dentro de las edades es: "+str(edad))
    elif comando[1].lower() == "promedio":
        for i in range(len(BD)):
            if float(BD[i][3]) < promedio:
                promedio = BD[i][3]
        print("El valor mínimo dentro de los promedios es: " + str(promedio))
    else:
        print("Comando de minimizar no valido")

def Suma(comando):
    edad = 0
    promedio = 0.0
    comando = comando.split(" ")
    if comando[1].lower() == "edad":
        for i in range(len(BD)):
            edad+=int(BD[i][1])
        print("La suma total de las edades es: "+str(edad))
    elif comando[1].lower() == "promedio":
        for i in range(len(BD)):
            promedio+=float(BD[i][3])
        print("La suma total de los promedios es: " + str(round(promedio,3)))
    else:
        print("Comando suma no valido")

def Cuenta():
    if len(BD) == 0:
        print("No se han cargado registros al sistema")
    else:
        print("Actualmente el sistema tiene "+str(len(BD))+" registros en el sistema")

def Reporte(comando):
    comando = comando.split(" ")
    try:
        if int(comando[1]) <= int(len(BD)):
            file = open("Reporte.html", "w")
            file.write("<!DOCTYPE html>\n")
            file.write('<html lang="en">\n')
            file.write('<head>\n')
            file.write('<style type="text/css">\n')
            file.write(
                'table { border: black 5px solid; border-collapse: collapse;   table-layout: auto; width: 100%; border-collapse: collapse; }\n')
            file.write(
                'body { background-color: #ffdd90; background-image: url("https://lh3.googleusercontent.com/proxy/N8cSinoTJKagEAw7ZcXlkjitj31O0IlYCkVUg5-tLaxAkoU-7hl1dpENdRSBx2mh2dDw6Nt0IqLDaZOm8SY4lzw3FMyGZVOOgffThgKz5h2eVMjG"); }\n')
            file.write('html { font-family: "helvetica neue", helvetica, arial, sans-serif; }')
            file.write(
                'tbody tr:nth-child(odd) { background-color: #42DCF8; } tbody tr:nth-child(even) { background-color: #659BFA; } table { background-color: #05FD5B; }')
            file.write('</style>\n')
            file.write('<meta charset="UTF-8">\n')
            file.write('<title>Registros</title>\n')
            file.write('</head>\n')
            file.write('<body>\n')
            file.write('<font face="Brush Script MT"><marquee behavior=alternate><h1>Simpleql</h1></marquee></font>\n')
            file.write('<p>Estos son los primeros ' + comando[1] + ' registros</p>\n')
            file.write('<div style="text-align:center;">\n')
            file.write('<table class="table table-dark" border="">\n')
            file.write('<thead>\n')
            file.write('<tr>\n')
            file.write('<th scope="col"><h2>#</h2></th>\n')
            file.write('<th scope="col"><h2>Nombre</h2></th>\n')
            file.write('<th scope="col"><h2>Edad</h2></th>\n')
            file.write('<th scope="col"><h2>Activo</h2></th>\n')
            file.write('<th scope="col"><h2>Promedio</h2></th>\n')
            file.write('</tr>\n')
            file.write('</thead>\n')
            file.write('<tbody>\n')
            for i in range(int(comando[1])):
                file.write('<tr>\n')
                file.write('<th scope="row">' + str(i + 1) + '</th>\n')
                file.write('<td>' + str(BD[i][0]) + '</td>\n')
                file.write('<td>' + str(BD[i][1]) + '</td>\n')
                file.write('<td>' + str(BD[i][2]) + '</td>\n')
                file.write('<td>' + str(BD[i][3]) + '</td>\n')
                file.write('</tr>\n')
            file.write('</tbody>\n')
            file.write('</table>\n')
            file.write('</div>')
            file.write('</body>\n')
            file.write('</html>\n')
            file.close()
            print("REPORTE GENERADO CON ÉXITO")
            webbrowser.open("Reporte.html")
        else:
            print("La cantidad de datos solicitada es mayor a la cantidad de registros existentes")
    except:
        print("Comando reportar no valido")

while comando != "salir":
    comando = input("Ingrese un comando: ")
    if comando[0:6].lower() == "cargar":
        cargar(comando)
    elif comando[0:12].lower() == "seleccionar ":
        Seleccionar(comando)
    elif comando[0:6].lower() == "maximo":
        if len(BD) == 0:
            print("Aun no existen registros en el sistema")
        else:
            Maximo(comando)
    elif comando[0:6].lower() == "minimo":
        if len(BD) == 0:
            print("Aun no existen registros en el sistema")
        else:
            Minimo(comando)
    elif comando[0:4].lower() == "suma":
        if len(BD) == 0:
            print("Aun no existen registros en el sistema")
        else:
            Suma(comando)
    elif comando[0:6].lower() == "cuenta":
        if len(BD) == 0:
            print("Aun no existen registros en el sistema")
        else:
            Cuenta()
    elif comando[0:8].lower() == "reportar":
        if len(BD) == 0:
            print("Aun no existen registros en el sistema")
        else:
            Reporte(comando)
    elif comando[0:5].lower() == "salir":
        print("Fin del programa \n Gracias por utilizar SimpleQl :D")
        break
    else:
        print("Comando no reconocido")