import lista

        

#Função de votação
def votacao():	
    governador=int(input("Digite o numero do candidato a Governador (ou 0 para Em Branco):  "))   
    if governador == 6:
        lista.candidato_escolhido(lista.governador6)
        d = lista.confirmar_voto()
        if d == ('s'):
            lista.voto6+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    #VOTO EM BRANCO/GOVERNADORES
    elif governador == 0:
        print("Deseja votar em Branco?")
        d = lista.confirmar_voto()
        if d == ('s'):
            lista.branco2+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    elif governador == 7:
        lista.candidato_escolhido(lista.governador7)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto7+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")  

    elif governador == 8:
        lista.candidato_escolhido(lista.governador8)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto8+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    elif governador == 9:
        lista.candidato_escolhido(lista.governador9)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto9+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    elif governador == 10:
        lista.candidato_escolhido(lista.governador10)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto10+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")	

    #NULO/GOVERNADORES
    else:
        d=input("Deseja votar nulo? s/n: ")
        if d == ('s'):
            lista.nulo2+=1
            print("Voto nulo registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")	
    
    #INPUT/PRESIDENTES
    presidente= int(input('Digite o numero do candidato a Presidente (ou 0 para Em Branco):   '))
    if presidente == 1:
        lista.candidato_escolhido(lista.presidente1)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto1+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")
    
    #VOTO EM BRANCO/PRESIDENTES
    elif presidente == 0:
        print("Deseja votar em Branco?")
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.branco1+=1
            print("Voto registrado com sucesso.       ")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    elif presidente== 2:
        lista.candidato_escolhido(lista.presidente2)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto2+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")

    elif presidente == 3:
        lista.candidato_escolhido(lista.presidente3)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto3+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    elif presidente == 4:
        lista.candidato_escolhido(lista.presidente4)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto4+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")

    elif presidente == 5:
        lista.candidato_escolhido(lista.presidente5)
        d =lista.confirmar_voto()
        if d == ('s'):
            lista.voto5+=1
            print("Voto registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")
    
    #NULO/PRESIDENTES
    else:
        d=input("Deseja votar nulo? s/n: ")
        if d == ('s'):
            lista.nulo1+=1 
            print("Voto nulo registrado com sucesso.")
        elif d == ('n'):
            print("Voto cancelado.")
        else:
            print("Comando incorreto!")	 


   