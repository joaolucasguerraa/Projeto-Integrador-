
import funcao

#Imprimir votos
def apurar_votos():
    print("Apuração dos votos: ")
    print("-" * 38)	
    print("          Pesidentes")
    print("-" * 38)	
    print("Votos do(a) candidato(a) %s: %i " %(presidente1,voto1))
    print("Votos do(a) candidato(a) %s: %i " %(presidente2,voto2))
    print("Votos do(a) candidato(a) %s: %i " %(presidente3,voto3))
    print("Votos do(a) candidato(a) %s: %i " %(presidente4,voto4))
    print("Votos do(a) candidato(a) %s: %i " %(presidente5,voto5))
    print("Votos em nulo: %i " %(nulo1))
    print("Votos em Branco: %i " %(branco1))
    print("")
    print("-" * 38)	
    print("         Governadores")
    print("-" * 38)	
    print("Votos do(a) candidato(a) %s: %i " %(governador6,voto6))
    print("Votos do(a) candidato(a) %s: %i " %(governador7,voto7))
    print("Votos do(a) candidato(a) %s: %i " %(governador8,voto8))
    print("Votos do(a) candidato(a) %s: %i " %(governador9,voto9))
    print("Votos do(a) candidato(a) %s: %i " %(governador10,voto10))
    print("Votos em nulo: %i " %(nulo2))
    print("Votos em Branco: %i " %(branco2))
    print("")
    
#IMPRIMI Candidatos
def lista_candidatos ():
    print("-" * 38)	
    print("Pesidentes")
    print("-" * 38)	
    print("Candidato(a)  1: %s" %(presidente1))
    print("Candidato(a)  2: %s" %(presidente2))
    print("Candidato(a)  3: %s" %(presidente3))
    print("Candidato(a)  4: %s" %(presidente4))
    print("Candidato(a)  5: %s" %(presidente5))
    print("")
    print("-" * 38)	
    print("Governadores")
    print("-" * 38)	
    print("Candidato(a)  6: %s" %(governador6))
    print("Candidato(a)  7: %s" %(governador7))
    print("Candidato(a)  8: %s" %(governador8))
    print("Candidato(a)  9: %s" %(governador9))
    print("Candidato(a) 10: %s" %(governador10)) 
    print("")

#Retorna canditado escolhido
def candidato_escolhido (a):
  print("Candidato escolhido: %s " %(a))

#def Confirmar voto
def confirmar_voto ():
	return(str(input("Confirmar voto? s/n: ")))

#IMPRIMI MENU
def menu ():

    print("URNA ELETRÔNICA DE VALENTINE")

    print("(1) Opção 1: listar candidatos.")

    print("(2) Opção 2: iniciar votação.")

    print("(3) Opção 3: apurar votos.")

    print("(4) Opção 4: desligar a urna.")



#NOMES GOVERNADORES 
governador6=('Leopold Strauss')
governador7=('Bill Williamson')
governador8=('Sean Macguire')
governador9=('Lenny Summers')
governador10=('Reverend Swanson')

#NOMES PRESIDENTES
presidente1=('Arthur Morgan')
presidente2=('Sadie Adler')
presidente3=('John Marston')
presidente4=('Dutch van der Linde')
presidente5=('Micah Bell')

voto1=0
voto2=0
voto3=0
voto4=0
voto5=0
voto6=0
voto7=0
voto8=0
voto9=0
voto10=0
nulo1=0
nulo2=0
branco2=0
branco1=0

