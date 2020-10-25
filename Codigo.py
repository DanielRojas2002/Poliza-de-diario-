#Listas de los cargos de cada cuenta
Cargos1000 = [0]
Cargos1001 = [0]
Cargos1002 = [0]
Cargos1003 = [0]
Cargos1004 = [0]
Cargos1005 = [0]
Cargos1006 = [0]
Cargos1007 = [0]
Cargos1008 = [0]
Cargos1009 = [0]
#Listas de abonos de las cuentas
Abonos1000 = [0]
Abonos1001 = [0]
Abonos1002 = [0]
Abonos1003 = [0]
Abonos1004 = [0]
Abonos1005 = [0]
Abonos1006 = [0]
Abonos1007 = [0]
Abonos1008 = [0]
Abonos1009 = [0]
#Suma de cada listas
BanCargos=0
BanAbonos=0
ProvCargos=0
ProvAbonos=0
TerrCargos=0
TerrAbonos=0
InvCargos=0
InvAbonos=0
EdiCargos=0
EdiAbonos=0
EqcomCargos=0
EqcomAbonos=0
EqtransCargos=0
EqtransAbonos=0
CapCargos=0
CapAbonos=0
GastoCargos=0
GastoAbonos=0
CostoCargos=0
CostoAbonos=0
#Total de cada cuenta
BancoTot=0
ProvTot=0
TerrTot=0
InvTot=0
EdiTot=0
EqcomTot=0
EqtransTot=0
CapTot=0
GastoTot=0
CostoTot=0
separador=("*"*30,"////","*"*30)
# Variable que tiene las cuentas
Cuentas =("1000)Bancos   \n1001)Proveedores \n1002)Terreno  \n1003)Almacen/Inventario \n1004)Edificio  \n1005)Eq Computo \n1006)Eq Transporte  \n1007)Capital Social \n1008)Gasto Ventas  \n1009)Costo Ventas")
#Variables definidas
Cuenta=0
Eleccion=0
SCA=0 #SELECCION PARA HACER CARGOS
pop= True;  #Variable para que cicle el menu

while pop ==True:
    print("")
    print("________________________________________________________________")
    print("                            MENU                                ")
    print("________________________________________________________________")
    Menu = ("1) Registrar un nuevo movimiento \n2) Obtener el saldo de una cuenta especifica \n3) Salir ")
    print (Menu)
    print(separador)
    op = int(input("Ingrese el numero de la opcion deseada: "))
    print(separador)  #Op es la variable de las opciones
#Opcion 1______________________________________________________________________________________________________________
    if op == 1:
        print("")
        print("________________________________________________________________")
        print("                 1) REGISTRAR MOVIMIENTO                        ")
        print("________________________________________________________________")
        print(Cuentas)
        Cuenta = int(input("Ingrese el codigo de la cuenta deseada: "))
        print(separador)
        #Aqui inicia la cuenta de banco
        if Cuenta ==1000:
            print("Cuenta seleccionada:Bancos")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero d iferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1000:
                        cargos1000 = int(input("Ingrese la cantidad: "))
                        Cargos1000.append(cargos1000)
                        if cargos1000==0:
                            break
                    BanCargos = sum(Cargos1000)
                    BancoTot=(BanCargos-BanAbonos)
                    print(separador)
                    print(f"Banco= {BancoTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1000:
                        abonos1000 = int(input("Ingrese la cantidad: "))
                        Abonos1000.append(abonos1000)
                        if abonos1000==0:
                            break
                    BanAbonos = sum(Abonos1000)
                    BancoTot=(BanCargos-BanAbonos)
                    print(separador)
                    print(f"Banco= {BancoTot}")
                    print(separador)
                    break
                #Aqui inicia la cuenta de Provedores
        elif Cuenta ==1001:
            print("Cuenta seleccionada:Proveedores")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1001:
                        cargos1001 = int(input("Ingrese la cantidad: "))
                        Cargos1001.append(cargos1001)
                        if cargos1001==0:
                            break
                    ProvCargos = sum(Cargos1001)
                    ProvTot=(ProvCargos-ProvAbonos)
                    print(separador)
                    print(f"Proveedores= {ProvTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1001:
                        abonos1001 = int(input("Ingrese la cantidad: "))
                        Abonos1001.append(abonos1001)
                        if abonos1001==0:
                            break
                    ProvAbonos = sum(Abonos1001)
                    ProvTot=(ProvCargos-ProvAbonos)
                    print(separador)
                    print(f"Proveedores= {ProvTot}")
                    print(separador)
                    break
                #Aqui inicia la cuenta de Terreno
        elif Cuenta ==1002:
            print("Cuenta seleccionada:Terreno")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1002:
                        cargos1002 = int(input("Ingrese la cantidad: "))
                        Cargos1002.append(cargos1002)
                        if cargos1002==0:
                            break
                    TerrCargos = sum(Cargos1002)
                    TerrTot=(TerrCargos-TerrAbonos)
                    print(separador)
                    print(f"Terreno= {TerrTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1002:
                        abonos1002 = int(input("Ingrese la cantidad: "))
                        Abonos1002.append(abonos1002)
                        if abonos1002==0:
                            break
                    TerrAbonos = sum(Abonos1002)
                    TerrTot=(TerrCargos-TerrAbonos)
                    print(separador)
                    print(f"Terreno= {TerrTot}")
                    print(separador)
                    break
                #Aqui inicia la cuenta de Almacen/Inventario
        elif Cuenta ==1003:
            print("Cuenta seleccionada:Almacen/Inventario")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n":))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1003:
                        cargos1003 = int(input("Ingrese la cantidad: "))
                        Cargos1003.append(cargos1003)
                        if cargos1003==0:
                            break
                    InvCargos = sum(Cargos1003)
                    InvTot=(InvCargos-InvAbonos)
                    print(separador)
                    print(f"Almacen/Inventario= {InvTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1003:
                        abonos1003 = int(input("Ingrese la cantidad: "))
                        Abonos1003.append(abonos1003)
                        if abonos1003==0:
                            break
                    InvAbonos = sum(Abonos1003)
                    InvTot=(InvCargos-InvAbonos)
                    print(separador)
                    print(f"Almacen/Inventario= {InvTot}")
                    print(separador)
                    break        
        #Aqui inicia la cuenta de Edificios
        elif Cuenta ==1004:
            print("Cuenta seleccionada:Edificio")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1004:
                        cargos1004 = int(input("Ingrese la cantidad: "))
                        Cargos1004.append(cargos1004)
                        if cargos1004==0:
                            break
                    EdiCargos = sum(Cargos1004)
                    EdiTot=(EdiCargos-EdiAbonos)
                    print(separador)
                    print(f"Almacen/Edientario= {EdiTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1004:
                        abonos1004 = int(input("Ingrese la cantidad: "))
                        Abonos1004.append(abonos1004)
                        if abonos1004==0:
                            break
                    EdiAbonos = sum(Abonos1004)
                    EdiTot=(EdiCargos-EdiAbonos)
                    print(separador)
                    print(f"Almacen/Edientario= {EdiTot}")
                    print(separador)
                    break
                      
        #Aqui inicia la cuenta de Equipo de computo
        elif Cuenta ==1005:
            print("Cuenta seleccionada:Eq de Computo")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1005:
                        cargos1005 = int(input("Ingrese la cantidad: "))
                        Cargos1005.append(cargos1005)
                        if cargos1005==0:
                            break
                    EqcomCargos = sum(Cargos1005)
                    EqcomTot=(EqcomCargos-EqcomAbonos)
                    print(f"Equipo de Computo= {EqcomTot}")
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1005:
                        abonos1005 = int(input("Ingrese la cantidad: "))
                        Abonos1005.append(abonos1005)
                        if abonos1005==0:
                            break
                    EqcomAbonos = sum(Abonos1005)
                    EqcomTot=(EqcomCargos-EqcomAbonos)
                    print(separador)
                    print(f"Almacen/Eqcomentario= {EqcomTot}")
                    print(separador)
                    break        
        
        
        #Aqui inicia la cuenta de Equipo de Transporte
        elif Cuenta ==1006:
            print("Cuenta seleccionada:Eq de transporte")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1006:
                        cargos1006 = int(input("Ingrese la cantidad: "))
                        Cargos1006.append(cargos1006)
                        if cargos1006==0:
                            break
                    EqtransCargos = sum(Cargos1006)
                    EqtransTot=(EqtransCargos-EqtransAbonos)
                    print(separador)
                    print(f"Almacen/Eqtransentario= {EqtransTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1006:
                        abonos1006 = int(input("Ingrese la cantidad: "))
                        Abonos1006.append(abonos1006)
                        if abonos1006==0:
                            break
                    EqtransAbonos = sum(Abonos1006)
                    EqtransTot=(EqtransCargos-EqtransAbonos)
                    print(separador)
                    print(f"Almacen/Eqtransentario= {EqtransTot}")
                    print(separador)
                    break
                
                
        #Aqui inicia la cuenta de Equipo de Capital Social
        elif Cuenta ==1007:
            print("Cuenta seleccionada:Capital Social")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1007:
                        cargos1007 = int(input("Ingrese la cantidad: "))
                        Cargos1007.append(cargos1007)
                        if cargos1007==0:
                            break
                    CapCargos = sum(Cargos1007)
                    CapTot=(CapCargos-CapAbonos)
                    print(separador)
                    print(f"Almacen/Capentario= {CapTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1007:
                        abonos1007 = int(input("Ingrese la cantidad: "))
                        Abonos1007.append(abonos1007)
                        if abonos1007==0:
                            break
                    CapAbonos = sum(Abonos1007)
                    CapTot=(CapCargos-CapAbonos)
                    print(separador)
                    print(f"Almacen/Capentario= {CapTot}")
                    print(separador)
                    break
                
        #Aqui inicia la cuenta de Equipo de Gastos de Venta
        elif Cuenta ==1008:
            print("Cuenta seleccionada:Gastos de Venta")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1008:
                        cargos1008 = int(input("Ingrese la cantidad: "))
                        Cargos1008.append(cargos1008)
                        if cargos1008==0:
                            break
                    GastoCargos = sum(Cargos1008)
                    GastoTot=(GastoCargos-GastoAbonos)
                    print(separador)
                    print(f"Almacen/Gastoentario= {GastoTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1008:
                        abonos1008 = int(input("Ingrese la cantidad: "))
                        Abonos1008.append(abonos1008)
                        if abonos1008==0:
                            break
                    GastoAbonos = sum(Abonos1008)
                    GastoTot=(GastoCargos-GastoAbonos)
                    print(separador)
                    print(f"Almacen/Gastoentario= {GastoTot}")
                    print(separador)
                    break        
        
        
        
        #Aqui inicia la cuenta de Equipo de Costos de Venta
        elif Cuenta ==1009:
            print("Cuenta seleccionada:Costos de Venta")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                SCA = int(input("Para hacer un cargo seleccione #1\nPara hacer un abono seleccione #2\n:"))
                if SCA ==1:
                    print("Para terminar de hacer un cargo ingrese 0")
                    for i in Cargos1009:
                        cargos1009 = int(input("Ingrese la cantidad: "))
                        Cargos1009.append(cargos1009)
                        if cargos1009==0:
                            break
                    CostoCargos = sum(Cargos1009)
                    CostoTot=(CostoCargos-CostoAbonos)
                    print(separador)
                    print(f"Almacen/Costoentario= {CostoTot}")
                    print(separador)
                    break
                elif SCA ==2:
                    print("Para terminar de hacer un abono ingrese 0")
                    for i in Abonos1009:
                        abonos1009 = int(input("Ingrese la cantidad: "))
                        Abonos1009.append(abonos1009)
                        if abonos1009==0:
                            break
                    CostoAbonos = sum(Abonos1009)
                    CostoTot=(CostoCargos-CostoAbonos)
                    print(separador)
                    print(f"Almacen/Costoentario= {CostoTot}")
                    print(separador)
                    break
    


    #Opcion 2______________________________________________________________________________________________________________
    elif op == 2:
        print("________________________________________________________________")
        print("                   2) SALDOS DE CUENTAS                         ")
        print("________________________________________________________________")
        print(Cuentas)
        Cuenta2 = int(input("Ingrese el codigo de la cuenta deseada: "))
        print(separador)
        #Total del banco
        if Cuenta2 ==1000:
            print("Cuenta seleccionada:Bancos")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Banco={BancoTot}")
                print(separador)
                break
        #Total de Proveedores
        if Cuenta2 ==1001:
            print("Cuenta seleccionada:Proveedores")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Proveedores={ProvTot}")
                print(separador)
                break
        #Total de Terreno
        if Cuenta2 ==1002:
            print("Cuenta seleccionada:Terreno")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Terreno={TerrTot}")
                print(separador)
                break
        #Total de Almacen
        if Cuenta2 ==1003:
            print("Cuenta seleccionada:Almacen/Inventario")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Almacen/Inventario={InvTot}")
                print(separador)
                break
        #Total de Edificios
        if Cuenta2 ==1004:
            print("Cuenta seleccionada:Edificio")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Edificio={EdiTot}")
                print(separador)
                break
        #Total de Equipo e computo
        if Cuenta2 ==1005:
            print("Cuenta seleccionada:Equipo de Computo")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Equipo de Computo={EqcomTot}")
                print(separador)
                break    
        #Total de Equipo de Transporte
        if Cuenta2 ==1006:
            print("Cuenta seleccionada:Equipo de Transporte")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Equipo de Transporte={EqtransTot}")
                print(separador)
                break    
        #Total de Capital Social
        if Cuenta2 ==1007:
            print("Cuenta seleccionada:Capital Social")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Capital Social={CapTot}")
                print(separador)
                break    
        #Total de Gasto de Ventas
        if Cuenta2 ==1008:
            print("Cuenta seleccionada:Gastos de Ventas")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Gastos de Ventas={GastoTot}")
                print(separador)
                break    
        #Total de Costo de Ventas
        if Cuenta2 ==1009:
            print("Cuenta seleccionada:Costo de Ventas")
            Eleccion = int(input("Si su cuenta es correcta ingrese #1 \nSi su cuenta es incorrecta ingrese un numero diferente a 1\n:"))
            while  Eleccion == 1:
                print(f"Costo de Ventas={CostoTot}")
                print(separador)
                break 
    

    #Opcion 3______________________________________________________________________________________________________________
    elif op == 3:
         pop =False
         print(separador)
         print("FIN DEL PROCESO :) ")
         print(separador)