import functions
print("*****************************")
print("Welcome to our city register!")
print("*****************************")


    
print ("Please select an option: ")
print("1. Add a new city")
print("2. Modify city information")
print("3. Delete a city")
print("4. Find a city using specific criteria")
 
opc=int(input(""))
 
if opc==1:
    functions.registrar_ciudades()        
elif opc==2:
    print("Coming soon!")     
elif opc==3:
    functions.eliminar_ciudad()
