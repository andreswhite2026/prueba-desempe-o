gestion = {
    1: {
        "id": 1048229292,
        "name": "andres",
        "curse": "riwi",
        "age": 30,
        "state": "asset"

    },
    2: {
        "id": 1048229296,
        "name": "luisa",
        "curse": "tecnologo",
        "age": 23,
        "state": "idle"
    },
    3: {
        "id": 1048229297,
        "name": "maria",
        "curse": "riwi",
        "age": 19,
        "state": "asset"
    },
    4: {
        "id": 1048229297,
        "name":"carlos",
        "curse": "riwi",
        "age": 17,
        "state": "idle"
    }
}
nombre = None
edad = None
curso = None
i_d = None
estado = None
seleccion = None
seleccion2 = None
borrar = None

def menu ():

    return int(input("What do you want to do? \n1.Register a new student \n2.View the list \n3.Search for a student \n4.Delete a student \n5.Update a student's information \n6.Exit \n: "))

def agregar (nombre:str, edad:int, curso:str, i_d:int, estado:str):
    nombre = input("Enter the name: ")
    edad = int(input("Enter the age: "))
    curso =input("Enter the course you are taking: ")
    i_d = int(input("Enter the id: "))
    estado = input("Enter the status, whether it is idle or asset: ")
    
    gestion[5] = {"id":i_d, "name":nombre, "curse":curso,"age": edad, "state": estado}
    print("added successfully\n")
    return nombre, edad, curso, i_d, estado

def mostrar ():
    print(gestion)

def buscar (i_d:int, edad:int, nombre:str):
    elige = int(input("Please tell me who you want to search for based on a specific criterion: \n1.id \n2.age \n3.name \n: "))
    if elige == 1:
        numero = int(input("please tell me the student id: "))
        busqueda_id = numero
        coder_encontrado = None

        for buscar, estudiante in gestion.items():
            if estudiante["id"] == busqueda_id:
                coder_encontrado = estudiante

        print(coder_encontrado)



        for buscar, estudiante in gestion.items():
            if estudiante["id"] == busqueda_id:
                print("Encontrado")
                continue
    elif elige == 2:
        numero2 = int(input("Porfavor digite la edad del estudiante: "))
        busqueda_age = numero2
        coder_encontrado = None

        for buscar, estudiante in gestion.items():
            if estudiante["age"] == busqueda_age:
                coder_encontrado = estudiante
        print(coder_encontrado)


        for buscar, estudiante in gestion.items():
            if estudiante["age"] == busqueda_age:
                print("Encontrado")
                continue    
    elif elige == 3:
        numero3 = input("Porfavor ingrese el nombre del estudiante: ")
        busqueda_name = numero3
        coder_encontrado = None

        for buscar, estudiante in gestion.items():
            if estudiante["name"] == busqueda_id:
                coder_encontrado = estudiante

        print(coder_encontrado)



        for buscar, estudiante in gestion.items():
            if estudiante["name"] == busqueda_id:
                print("Encontrado")
                continue
    return i_d, edad, nombre

def modificar (seleccion2:int, seleccion:str, nombre:str, edad:int, curso:str, i_d:int, estado:str):
    seleccion = input("Tell me which student you want to modify? andres, luisa, maria, carlos:")
    if seleccion == "luisa":
        seleccion2 = int(input("Tell me what you want to change about Luisa? \n1.id \n2.name \n3.curse \n4.age \n5.state \n: "))
        if seleccion2 == 1:
            i_d = int(input("Enter the new id: "))
            gestion[2]["id"] = (i_d)
        elif seleccion2 == 2:
            nombre = input("Enter the new name: ")
            gestion[2]["name"] = (nombre)
        elif seleccion2 == 3:
            curso = input("Enter the new curse: ")
            gestion[2]["curse"] = (curso)
        elif seleccion2 == 4:
            edad = int(input("Enter the new age: "))
            gestion[2]["age"] = (edad)
        elif seleccion2 == 5:
            estado = input("Enter the new state: ")
            gestion [2]["state"] = (estado)
            
    elif seleccion == "andres":
        seleccion2 = int(input("Tell me what you want to change about Luisa? \n1.id \n2.name \n3.curse \n4.age \n5.state \n: "))
        if seleccion2 == 1:
            i_d = int(input("Enter the new id: "))
            gestion[1]["id"] = (i_d)
        elif seleccion2 == 2:
            nombre = input("Enter the new name: ")
            gestion[1]["name"] = (nombre)
        elif seleccion2 == 3:
            curso = input("Enter the new curse: ")
            gestion[1]["curse"] = (curso)
        elif seleccion2 == 4:
            edad = int(input("Enter the new age: "))
            gestion[1]["age"] = (edad)
        elif seleccion2 == 5:
            estado = input("Enter the new state: ")
            gestion [1]["state"] = (estado)    
    
    elif seleccion == "maria":
        seleccion2 = int(input("Tell me what you want to change about Luisa? \n1.id \n2.name \n3.curse \n4.age \n5.state \n: "))
        if seleccion == 1:
            i_d = int(input("Enter the new id: "))
            gestion[3]["id"] = (i_d)
        elif seleccion2 == 2:
            nombre = input("Enter the new name: ")
            gestion[3]["name"] = (nombre)
        elif seleccion2 == 3:
            curso = input("Enter the new curse: ")
            gestion[3]["curse"] = (curso)
        elif seleccion2 == 4:
            edad = int(input("Enter the new age: "))
            gestion[3]["age"] = (edad)
        elif seleccion2 == 5:
            estado = input("Enter the new state: ")
            gestion [3]["state"] = (estado)    
    
    elif seleccion == "carlos":
        seleccion2 = int(input("Tell me what you want to change about Luisa? \n1.id \n2.name \n3.curse \n4.age \n5.state \n: "))
        if seleccion2 == 1:
            i_d = int(input("Enter the new id: "))
            gestion[4]["id"] = (i_d)
        elif seleccion2 == 2:
            nombre = input("Enter the new name: ")
            gestion[4]["name"] = (nombre)
        elif seleccion2 == 3:
            curso = input("Enter the new curse: ")
            gestion[4]["curse"] = (curso)
        elif seleccion2 == 4:
            edad = int(input("Enter the new age: "))
            gestion[4]["age"] = (edad)
        elif seleccion2 == 5:
            estado = input("Enter the new state: ")
            gestion [4]["state"] = (estado)    
        return seleccion, seleccion2, nombre, edad, curso, i_d, estado

def eliminar (borrar:int):
    borrar = int(input("Porfavor digame a quien quiere borrar: \n1.andres \n2.luisa \n3.maria \n4.carlos \n: "))
    if borrar == 1:
        gestion[1].pop
    elif borrar == 2:
        gestion[2].pop
    elif borrar == 3:
        gestion[3].pop
    elif borrar == 4:
        gestion[4].pop

    return borrar


seguir = "si"
while seguir == "si":
    opcion = menu()
    if opcion == 1:
        agregar(nombre, edad, curso, i_d, estado)

    elif opcion == 2:
        mostrar()
    
    elif opcion == 3:
       seleccion = buscar(i_d, edad, nombre )
   
    elif opcion == 4:
        eliminar(borrar)
    
    elif opcion == 5:
        modificar (seleccion, seleccion2, nombre, edad, curso, i_d, estado)
    
    else:
        break
#

        