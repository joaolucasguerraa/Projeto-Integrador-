import lista
import funcao


operacao=0

while operacao != 4:
    lista.menu()
    operacao=int(input("Escolha sua opção: "))    
    
    if operacao == 1:
        lista.lista_candidatos()
    
    elif operacao == 2:
        funcao.votacao()
    
    elif operacao == 3:
        lista.apurar_votos()
    
    elif operacao != (4 or 1 or 2 or 3):
	    print("Opção inválida!")


#ENCERRAR A URNA	
print("A urna foi encerrada. Obrigado por utilizar a Urna Eletrônica de Valentine!")