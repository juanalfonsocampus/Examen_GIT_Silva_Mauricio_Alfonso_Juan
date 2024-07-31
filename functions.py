import json

ruta = "data.json"

def leer_datos_ciudades():
    try:
        with open(ruta, "r") as file:
            archivo = json.load(file)
            print("Information complete. Program ready to launch.")
            return archivo

    except FileNotFoundError:
        print("Sorry, we could not find that city!")

def guardar_datos_ciudades(data):
    with open("data.json", "w") as archivo:
        json.dump(data, archivo, indent=4)
    print("Saving...")


leer_datos_ciudades()

def registrar_ciudades():
    data = leer_datos_ciudades()
    while True:
        print("*********************************************************")
        print("Welcome to our city register")
        print("*********************************************************")
        city_name = input("Please write the name of the city you want to register: ")
        if city_name not in data["ciudades"]:

            country = input("Please the country in which the city you want to add is located: ")
            zip = int(input("Please write the zip code: "))
            population = int(input("Please write the population number of the city: "))
            data["ciudades"][city_name] = {
                "country" : country,
                "zip" : zip,
                "population" : population,
                # "ciudad" : True
            }
            guardar_datos_ciudades(data)
            print("THE CITY HAS BEEN SUCCESSFULLY STORED!")
            break
        else:
            print("That city has already been registered!")
            continue
        

    
        

def eliminar_ciudad():
    data = leer_datos_ciudades()
    while True:
        print("It seems like you want to delete a city!")
        print("*************************************************")
        city_name = input("Write the name of the city you want to delete: ")
        if city_name not in data["ciudades"]:
            print("That city does not exist in our register!")
        else:
            nombre_eliminado = data["ciudades"][city_name]["country"]
            opt = int(input(f"Are you sure you want to delete a city that belongs to {nombre_eliminado}? (1.HELL YES!/2.NO, SHIT): "))
            if opt == 1:
                data["ciudades"].pop(city_name, None)
                print("THE CITY HAS BEEN SUCCESSFULLY DELETED!")
                guardar_datos_ciudades(data)
                break
            elif opt == 2:
                print("Exiting...")
                break