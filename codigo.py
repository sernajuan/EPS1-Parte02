class Persona:
 def __init__(self, nom, dni, app):
         self.nom = nom
         self.dni=dni
         self.app=app
i=0
lista=[]  
while i==0:
    print("menu")
    print("1. Registrar ")
    print("2. Eliminar ")
    print("3. Editar") 
    print("4. Listar")
    print("5. Salir") 
    print("Ingrese la opcion") 
    opcion = int(input())
    if opcion==1:
        print("*****REGISTRAR****")
    elif opcion==2:
        print("*****ELIMINNAR*****")
        
    elif opcion==3:
        print("*****EDITAR*****")
    elif opcion==4:
        print("*****LISTAR*****")
        
    elif opcion==5:
        exit()
    else:
        print("Opcion invalida")